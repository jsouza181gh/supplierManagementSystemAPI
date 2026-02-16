from flask import Blueprint, request, jsonify
from services import userService

userBlueprint = Blueprint("user", __name__, url_prefix="/api/users")

@userBlueprint.route("/", methods=["POST"])
def createUser():
    requestData = request.get_json()
    newUser = userService.createUser(
        requestData.get("name"),
        requestData.get("lastName"),
        requestData.get("email"),
        requestData.get("password")
    )
    return jsonify(newUser), 201

@userBlueprint.route("/<userId>", methods=["GET"])
def getUser(userId):
    user = userService.findUserById(userId),
    return jsonify(user), 200

@userBlueprint.route("/<userId>", methods=["PUT"])
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
def deleteUser(userId):
    userService.deleteUser(userId)
    return "", 204