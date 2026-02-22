from services import userService
from schemas.userSchema import UserSchema, LoginSchema
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from pydantic import ValidationError

userBlueprint = Blueprint("user", __name__, url_prefix="/users")

@userBlueprint.route("/register", methods=["POST"])
def createUser():
    try:
        validUser = UserSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400

    newAcessToken = userService.createUser(
        validUser.name,
        validUser.lastName,
        validUser.email,
        validUser.password
    )
    return jsonify(accessToken=newAcessToken), 201

@userBlueprint.route("/login", methods=["POST"])
def login():
    try:
        validLogin = LoginSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    validatedToken = userService.validateLogin(
        validLogin.email,
        validLogin.password
    )
    return jsonify(accessToken=validatedToken), 200

@userBlueprint.route("/", methods=["GET"])
@jwt_required()
def getUser():
    userId = get_jwt_identity()
    user = userService.findUserById(userId)
    return jsonify(user), 200

@userBlueprint.route("/", methods=["PUT"])
@jwt_required()
def updateUser():
    try:
        validUser = UserSchema(**request.get_json())
    except ValidationError as e:
        return jsonify(
            {
                "errors" : e.errors(
                    include_context=False
                )
            }
        ), 400
    
    userId = get_jwt_identity()
    user = userService.updateUser(
        userId,
        validUser.name,
        validUser.lastName,
        validUser.email,
        validUser.password
    )
    return jsonify(user), 200

@userBlueprint.route("/", methods=["DELETE"])
@jwt_required()
def deleteUser():
    params = request.args
    if params.get("userId"):
        userId = params.get("userId")
    else:
        userId = get_jwt_identity()
    userService.deleteUser(userId)
    return "", 204