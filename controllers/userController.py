from flask import Blueprint, request, jsonify
from services import userService

userBlueprint = Blueprint("user", __name__, url_prefix="/api/user")

@userBlueprint.route("/", methods=["POST"])
def createUser():
    data = request.get_json()
    pass

@userBlueprint.route("/<userId>", methods=["GET"])
def getUser(userId):
    pass

@userBlueprint.route("/<userId>", methods=["PUT"])
def updateUser(userId):
    data = request.get_json()
    pass

@userBlueprint.route("/<userId>", methods=["DELETE"])
def deleteUser(userId):
    pass