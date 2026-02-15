from flask import Blueprint, request, jsonify
from services import supplierService

supplierBlueprint = Blueprint("supplier", __name__, url_prefix="/api/supplier")

@supplierBlueprint.route("/", methods=["POST"])
def createSupplier():
    data = request.get_json()
    pass

@supplierBlueprint.route("/<supplierId>", methods=["GET"])
def getSupplier(supplierId):
    pass

@supplierBlueprint.route("/<supplierId>", methods=["PUT"])
def updateSupplier(supplierId):
    data = request.get_json()
    pass

@supplierBlueprint.route("/<supplierId>", methods=["DELETE"])
def deleteSupplier(supplierId):
    pass