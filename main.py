from database import createDataBase
from services import userService

if __name__ == "__main__":
    createDataBase()
    userService.deleteUser("d6119e31-cbd2-4368-ac87-3a04a328e676")