from database import engine, Base
from entities import *

if __name__ == "__main__":
    Base.metadata.create_all(engine)