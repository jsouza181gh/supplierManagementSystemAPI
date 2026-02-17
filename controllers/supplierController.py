from services import supplierService
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

supplierBlueprint = Blueprint("supplier", __name__, url_prefix="/suppliers")

@supplierBlueprint.route("/", methods=["POST"])
@jwt_required()
def createSupplier():
    requestData = request.get_json()
    newSupplier = supplierService.createSupplier(
        requestData.get("name"), 
        requestData.get("cnpj"), 
        requestData.get("location"), 
        requestData.get("representative"), 
        requestData.get("phoneNumber"), 
        requestData.get("email"), 
        requestData.get("site"), 
        requestData.get("description"),
        requestData.get("itemIds")
    )
    return jsonify(newSupplier), 201

@supplierBlueprint.route("/<supplierId>", methods=["GET"])
@jwt_required()
def getSupplier(supplierId):
    supplier = supplierService.findSupplierById(supplierId)
    return jsonify(supplier), 200

@supplierBlueprint.route("/", methods=["GET"])
@jwt_required()
def loadSuppliers():
    params = request.args
    suppliers = supplierService.loadSuppliers(
        int(params.get("page", 1)),
        int(params.get("limit", 10)),
    )
    return jsonify(suppliers), 200

@supplierBlueprint.route("/<supplierId>", methods=["PUT"])
@jwt_required()
def updateSupplier(supplierId):
    requestData = request.get_json()
    supplier = supplierService.updateSupplier(
        supplierId,
        requestData.get("name"), 
        requestData.get("cnpj"), 
        requestData.get("location"), 
        requestData.get("representative"), 
        requestData.get("phoneNumber"), 
        requestData.get("email"), 
        requestData.get("site"), 
        requestData.get("description"),
        requestData.get("itemIds"),
        requestData.get("isPreferred")
    )
    return jsonify(supplier), 200


@supplierBlueprint.route("/<supplierId>", methods=["DELETE"])
@jwt_required()
def deleteSupplier(supplierId):
    supplierService.deleteSupplier(supplierId)
    return "", 204