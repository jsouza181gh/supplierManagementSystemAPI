from services import itemService
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

itemBlueprint = Blueprint("item", __name__, url_prefix="/items")

@itemBlueprint.route("/", methods=["POST"])
@jwt_required()
def createItem():
    requestData = request.get_json()
    newItem = itemService.createItem(
        requestData.get("name"),
        requestData.get("category"),
        requestData.get("supplierIds",[])
    )    
    return jsonify(newItem), 201

@itemBlueprint.route("/<itemId>", methods=["GET"])
@jwt_required()
def getItem(itemId):
    item = itemService.findItemById(itemId)
    return jsonify(item), 200

@itemBlueprint.route("/", methods=["GET"])
@jwt_required()
def loadItens():
    params = request.args
    items = itemService.loadItems(
        int(params.get("page", 1)),
        int(params.get("limit", 10)),
        params.get("search")
    )
    return jsonify(items), 200

@itemBlueprint.route("/<itemId>", methods=["PUT"])
@jwt_required()
def updateItem(itemId):
    requestData = request.get_json()
    item = itemService.updateItem(
        itemId,
        requestData.get("name"),
        requestData.get("category"),
        requestData.get("supplierIds")
    )
    return jsonify(item), 200

@itemBlueprint.route("/<itemId>", methods=["DELETE"])
@jwt_required()
def deleteItem(itemId):
    itemService.deleteItem(itemId)
    return "", 204