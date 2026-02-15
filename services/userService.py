from repositories import userRepository

def createUser(
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    
    newUser = userRepository.createUser(
        newName,
        newLastName,
        newEmail,
        newPassword
    )
    return newUser

def findUserById(userId : str):
    user = userRepository.findUserById(userId)
    return user

def updateUser(
        userId : str,
        newName : str,
        newLastName : str,
        newEmail : str,
        newPassword : str
    ):
    
    user = userRepository.updateUser(
        userId,
        newName,
        newLastName,
        newEmail,
        newPassword
    )
    return user

def deleteUser(userId : str):
    userRepository.deleteUser(userId)