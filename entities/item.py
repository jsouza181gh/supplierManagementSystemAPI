from database import Base
from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from entities.item_supplier import item_supplier

class Item(Base):
    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column("name", String(100), nullable=False)
    category = Column("category", String(100))

    suppliers = relationship(
        "Supplier",
        secondary=item_supplier,
        back_populates="items"
    )

    def __init__(self, name, category):
        self.name = name
        self.category = category