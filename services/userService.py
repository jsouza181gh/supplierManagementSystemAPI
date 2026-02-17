from repositories import userRepository
from flask_bcrypt import check_password_hash
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token

def createUser(
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    
    hashedPassword = generate_password_hash(newPassword).decode("utf-8")
    newUser = userRepository.createUser(
        newName,
        newLastName,
        newEmail,
        hashedPassword
    )
    accessToken = create_access_token(identity=newUser.id)
    return accessToken

def validateLogin(
        email : str,
        password : str
    ):
    user = userRepository.findUserByEmail(email)

    if not user:
        return {"NotFoundError" : "User was not found"}, 404

    validLogin = check_password_hash(user.password, password)

    if not validLogin:
        return {"Unauthorized": "Invalid credentials"}, 401
    
    accessToken = create_access_token(identity=user.id)
    return accessToken

def findUserById(userId : str):
    user = userRepository.findUserById(userId)
    return createDTO(user)

def updateUser(
        userId : str,
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    
    hashedPassword = generate_password_hash(newPassword).decode("utf-8")
    user = userRepository.updateUser(
        userId,
        newName,
        newLastName,
        newEmail,
        hashedPassword
    )
    return createDTO(user)

def deleteUser(userId : str):
    userRepository.deleteUser(userId)

def createDTO(user):
    return {
        "id" : user.id,
        "name" : user.name,
        "lastName" : user.lastName,
        "email" : user.email,
        "password" : user.password
    }