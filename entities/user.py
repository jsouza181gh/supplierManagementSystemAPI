from database import Base
from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column("name", String(100), nullable=False)
    lastName = Column("last_name", String(100), nullable=False)
    email = Column("email", String(100), unique=True, nullable=False)
    password = Column("password", String(255), nullable=False)

    def __init__(self, name, lastName, email, password):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password