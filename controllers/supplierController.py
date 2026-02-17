from services import supplierService
from schemas.supplierSchema import SupplierSchema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

supplierBlueprint = Blueprint("supplier", __name__, url_prefix="/suppliers")

@supplierBlueprint.route("/", methods=["POST"])
@jwt_required()
def createSupplier():
    try:
        validSupplier = SupplierSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    newSupplier = supplierService.createSupplier(
        validSupplier.name, 
        validSupplier.cnpj, 
        validSupplier.location, 
        validSupplier.representative, 
        validSupplier.phoneNumber, 
        validSupplier.email, 
        str(validSupplier.site), 
        validSupplier.description,
        validSupplier.itemIds
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
    try:
        validSupplier = SupplierSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    supplier = supplierService.updateSupplier(
        supplierId,
        validSupplier.name,
        validSupplier.cnpj,
        validSupplier.location,
        validSupplier.representative,
        validSupplier.phoneNumber,
        validSupplier.email,
        str(validSupplier.site),
        validSupplier.description,
        validSupplier.itemIds,
        validSupplier.isPreferred
    )
    return jsonify(supplier), 200

@supplierBlueprint.route("/<supplierId>", methods=["DELETE"])
@jwt_required()
def deleteSupplier(supplierId):
    supplierService.deleteSupplier(supplierId)
    return "", 204