from services import itemService
from schemas.itemSchema import ItemSchema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

itemBlueprint = Blueprint("item", __name__, url_prefix="/items")

@itemBlueprint.route("/", methods=["POST"])
@jwt_required()
def createItem():
    try:
        validItem = ItemSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    newItem = itemService.createItem(
        validItem.name,
        validItem.category,
        validItem.supplierIds
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
    try:
        validItem = ItemSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    item = itemService.updateItem(
        itemId,
        validItem.name,
        validItem.category,
        validItem.supplierIds
    )
    return jsonify(item), 200

@itemBlueprint.route("/<itemId>", methods=["DELETE"])
@jwt_required()
def deleteItem(itemId):
    itemService.deleteItem(itemId)
    return "", 204