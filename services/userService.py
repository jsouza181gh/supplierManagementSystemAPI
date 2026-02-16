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
    return createDTO(newUser)

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
    
    user = userRepository.updateUser(
        userId,
        newName,
        newLastName,
        newEmail,
        newPassword
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
        "passwrd" : user.password
    }