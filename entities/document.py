from datetime import datetime
from database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    supplierId = Column("supplier_id", UUID(as_uuid=True), ForeignKey("suppliers.id"), nullable=False)
    name = Column("name", String(100), nullable=False, unique=True)
    path = Column("path", String(255), nullable=False, unique=True)
    category = Column("category", String(100))
    createdAt = Column("created_at", DateTime, default=datetime.utcnow)

    supplier = relationship("Supplier", back_populates="documents")
    
    def __init__(self, name, path, category, supplierId):
        self.name = name
        self.path = path
        self.category = category
        self.supplierId = supplierId