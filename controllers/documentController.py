from services import documentService
from schemas.documentSchema import DocumentSchema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from pydantic import ValidationError
from supabaseClient import supabase
import json, hashlib, os

documentBlueprint = Blueprint("document", __name__, url_prefix="/documents")

@documentBlueprint.route("/", methods=["POST"])
@jwt_required()
def createDocument():
    requestFile = request.files.get("file")
    if not requestFile:
        return jsonify({"error": "File is required"}), 400
    
    rawData = request.form.get("data")
    if not rawData:
        return jsonify({"error": "Document data is required"}), 400
    
    try:
        requestData = json.loads(rawData)
    except json.JSONDecodeError:
        return jsonify({"error": "JSON inválido"}), 400
    
    try:
        validDocument = DocumentSchema(**requestData)
    except ValidationError as e:
        return jsonify({"errors" : e.errors(include_context=False)}), 400
    
    name = hashlib.sha256(requestFile.filename.encode('utf-8')).hexdigest()
    path = f"suppliers/{validDocument.supplierId}/{name}"
    bucket = os.getenv("SUPABASE_BUCKET_NAME")
    supabase.storage.from_(bucket).upload(
        path,
        requestFile.read(),
        {"content-type": requestFile.content_type}
    )
    
    document = documentService.createDocument(
       requestFile.filename,
       path,
       validDocument.category,
       validDocument.supplierId
    )
    return jsonify(document), 201

@documentBlueprint.route("/<documentId>", methods=["GET"])
@jwt_required()
def getDocument(documentId):
    document = documentService.findDocumentById(documentId)
    bucket = os.getenv("SUPABASE_BUCKET_NAME")
    signedUrl = (supabase.storage
        .from_(bucket)
        .create_signed_url(document['path'], 60)
        )

    return {"url": signedUrl["signedURL"], "name" : document['name']}, 200

@documentBlueprint.route("/", methods=["GET"])
@jwt_required()
def loadDocuments():
    params = request.args
    documents = documentService.loadSupplierDocuments(
        params.get("supplierId")
    )
    return jsonify(documents), 200

@documentBlueprint.route("/<documentId>", methods=["PUT"])
@jwt_required()
def updateDocument(documentId):
    document = documentService.findDocumentById(documentId)
    requestFile = request.files.get("file")
    if not requestFile:
        return jsonify({"error": "File is required"}), 400
    
    rawData = request.form.get("data")
    if not rawData:
        return jsonify({"error": "Document data is required"}), 400
    
    try:
        requestData = json.loads(rawData)
    except json.JSONDecodeError:
        return jsonify({"error": "JSON inválido"}), 400

    try:
        validDocument = DocumentSchema(**requestData)
    except ValidationError as e:
        return jsonify({"errors" : e.errors(include_context=False)}), 400
    
    documentPath = document["path"]
    name = hashlib.sha256(requestFile.filename.encode('utf-8')).hexdigest()
    newPath = f"suppliers/{document["supplierId"]}/{name}"
    bucket = os.getenv("SUPABASE_BUCKET_NAME")

    supabase.storage.from_(bucket).upload(
        newPath,
        requestFile.read(),
        {"content-type": requestFile.content_type}
    )

    document = documentService.updateDocument(
        documentId,
        requestFile.filename,
        newPath,
        validDocument.category
    )

    if documentPath != newPath:
        supabase.storage.from_(bucket).remove([documentPath])

    return jsonify(document), 200

@documentBlueprint.route("/<documentId>", methods=["DELETE"])
@jwt_required()
def deleteDocument(documentId):
    document = documentService.findDocumentById(documentId)
    bucket = os.getenv("SUPABASE_BUCKET_NAME")
    supabase.storage.from_(bucket).remove([document["path"]])
    documentService.deleteDocument(documentId)
    return "", 204