from database import session
from entities.user import User

def createUser(
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    newUser = User(
        name = newName,
        lastName = newLastName,
        email = newEmail,
        password = newPassword
    )
    session.add(newUser)
    session.commit()
    return newUser

def findUserById(userId : str):
    user = (
        session
        .query(User)
        .filter_by(id=userId)
        .first()
    )
    return user

def findUserByEmail(userEmail : str):
    user = (
        session
        .query(User)
        .filter_by(email=userEmail)
        .first()
    )
    return user

def updateUser(
        userId : str,
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    user = findUserById(userId)
    user.name = newName
    user.lastName = newLastName
    user.email = newEmail
    user.password = newPassword

    session.add(user)
    session.commit()
    return user


def deleteUser(userId : str):
    user = findUserById(userId)
    session.delete(user)
    session.commit()