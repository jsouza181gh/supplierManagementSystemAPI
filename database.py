import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require",
    pool_pre_ping=True
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

session = Session()
Base = declarative_base()

from entities.user import User
from entities.supplier import Supplier
from entities.item import Item
from entities.document import Document

def createDataBase():
    Base.metadata.create_all(engine)