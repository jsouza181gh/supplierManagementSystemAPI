from flask import Blueprint, request, jsonify
from services import supplierService

supplierBlueprint = Blueprint("supplier", __name__, url_prefix="/api/suppliers")

@supplierBlueprint.route("/", methods=["POST"])
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
def getSupplier(supplierId):
    supplier = supplierService.findSupplierById(supplierId)
    return jsonify(supplier), 200

@supplierBlueprint.route("/", methods=["GET"])
def loadSuppliers():
    suppliers = supplierService.loadSuppliers()
    return jsonify(suppliers), 200

@supplierBlueprint.route("/<supplierId>", methods=["PUT"])
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
def deleteSupplier(supplierId):
    supplierService.deleteSupplier(supplierId)
    return "", 204