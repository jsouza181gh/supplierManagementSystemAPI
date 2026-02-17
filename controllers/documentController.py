from services import documentService
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

documentBlueprint = Blueprint("document", __name__, url_prefix="/documents")

@documentBlueprint.route("/", methods=["POST"])
@jwt_required()
def createDocument():
    requestData = request.get_json()
    document = documentService.createDocument(
        requestData.get("name"),
        requestData.get("path"),
        requestData.get("category"),
        requestData.get("supplierId"),
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
    requestData = request.get_json()
    document = documentService.updateDocument(
        documentId,
        requestData.get("name"),
        requestData.get("path"),
        requestData.get("category")
    )
    return jsonify(document), 200

@documentBlueprint.route("/<documentId>", methods=["DELETE"])
@jwt_required()
def deleteDocument(documentId):
    documentService.deleteDocument(documentId)
    return "", 204