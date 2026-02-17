from services import userService
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

userBlueprint = Blueprint("user", __name__, url_prefix="/users")

@userBlueprint.route("/register", methods=["POST"])
def createUser():
    requestData = request.get_json()
    acessToken = userService.createUser(
        requestData.get("name"),
        requestData.get("lastName"),
        requestData.get("email"),
        requestData.get("password")
    )
    return jsonify(acessToken), 201

@userBlueprint.route("/login", methods=["POST"])
def login():
    requestData = request.get_json()
    validatedToken = userService.validateLogin(
        requestData.get("email"),
        requestData.get("password")
    )
    
    if validatedToken[1] in [401, 404]:
        errorMessage, errorCode = validatedToken
        return jsonify(errorMessage), errorCode
    
    return jsonify(acessToken=validatedToken), 200

@userBlueprint.route("/<userId>", methods=["GET"])
@jwt_required()
def getUser(userId):
    user = userService.findUserById(userId),
    return jsonify(user), 200

@userBlueprint.route("/<userId>", methods=["PUT"])
@jwt_required()
def updateUser(userId):
    requestData = request.get_json()
    user = userService.updateUser(
        userId,
        requestData.get("name"),
        requestData.get("lastName"),
        requestData.get("email"),
        requestData.get("password")
    )
    return jsonify(user), 200

@userBlueprint.route("/<userId>", methods=["DELETE"])
@jwt_required()
def deleteUser(userId):
    userService.deleteUser(userId)
    return "", 204