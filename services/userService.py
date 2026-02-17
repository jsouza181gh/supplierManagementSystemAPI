from repositories import userRepository
from exceptions import NotFoundException, UnauthorizedException, ConflictException, BadRequestException
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import check_password_hash
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token
from uuid import UUID

def createUser(
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    hashedPassword = generate_password_hash(newPassword).decode("utf-8")
    try:
        newUser = userRepository.createUser(
            newName,
            newLastName,
            newEmail,
            hashedPassword
        )
    except IntegrityError:
        raise ConflictException("User already exists")
    
    accessToken = create_access_token(identity=newUser.id)
    return accessToken

def validateLogin(
        email : str,
        password : str
    ):
    user = userRepository.findUserByEmail(email)

    if not user:
        raise NotFoundException("User was not found")

    validLogin = check_password_hash(user.password, password)

    if not validLogin:
        raise UnauthorizedException()
    
    accessToken = create_access_token(identity=user.id)
    return accessToken

def findUserById(userId : str):
    isValidId(userId)
    user = userRepository.findUserById(userId)

    if not user:
        raise NotFoundException("User was not found")
    
    return createDTO(user)

def updateUser(
        userId : str,
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    isValidId(userId)
    hashedPassword = generate_password_hash(newPassword).decode("utf-8")
    try:
        user = userRepository.updateUser(
            userId,
            newName,
            newLastName,
            newEmail,
            hashedPassword
        )
    except IntegrityError:
        raise ConflictException("User already exists")
    
    if not user:
        raise NotFoundException("User was not found")
    
    return createDTO(user)

def deleteUser(userId : str):
    isValidId(userId)
    try:
        deleted = userRepository.deleteUser(userId)
    except IntegrityError:
        raise ConflictException("User cannot be deleted because it is in use")
    
    if not deleted:
        raise NotFoundException("User was not found")

def createDTO(user):
    return {
        "id" : user.id,
        "name" : user.name,
        "lastName" : user.lastName,
        "email" : user.email,
        "password" : user.password
    }

def isValidId(id: str):
    try:
        UUID(id)
        return True
    except (ValueError, AttributeError, TypeError):
        raise BadRequestException("Invalid ID")