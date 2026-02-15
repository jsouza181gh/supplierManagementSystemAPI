from database import Base
from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID

class Item(Base):
    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column("name", String(100), nullable=False)
    category = Column("category", String(100))

    def __init__(self, name, category):
        self.name = name
        self.category = category