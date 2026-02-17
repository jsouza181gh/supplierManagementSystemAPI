from services import documentService
from schemas.documentSchema import DocumentSchema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

documentBlueprint = Blueprint("document", __name__, url_prefix="/documents")

@documentBlueprint.route("/", methods=["POST"])
@jwt_required()
def createDocument():
    try:
        validDocument = DocumentSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    document = documentService.createDocument(
       validDocument.name,
       validDocument.path,
       validDocument.category,
       validDocument.supplierId,
    )
    return jsonify(document), 201

@documentBlueprint.route("/<documentId>", methods=["GET"])
@jwt_required()
def getDocument(documentId):
    document = documentService.findDocumentById(documentId)
    return jsonify(document), 200

@documentBlueprint.route("/", methods=["GET"])
@jwt_required()
def loadDocuments():
    params = request.args
    print(params.get("supplierId"))
    documents = documentService.loadSupplierDocuments(
        params.get("supplierId")
    )
    return jsonify(documents), 200

@documentBlueprint.route("/<documentId>", methods=["PUT"])
@jwt_required()
def updateDocument(documentId):
    try:
        validDocument = DocumentSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    document = documentService.updateDocument(
        documentId,
        validDocument.name,
        validDocument.path,
        validDocument.category
    )
    return jsonify(document), 200

@documentBlueprint.route("/<documentId>", methods=["DELETE"])
@jwt_required()
def deleteDocument(documentId):
    documentService.deleteDocument(documentId)
    return "", 204