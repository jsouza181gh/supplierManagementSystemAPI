from database import Base
from sqlalchemy import Column, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column("name", String(100), nullable=False)
    cnpj = Column("cnpj", String(100), unique=True, nullable=False)
    location = Column("location", String(100), nullable=False)
    representative = Column("representative", String(100), nullable=False)
    phoneNumber = Column("phone_number", String(100), nullable=False)
    email = Column("email", String(100), nullable=False)
    site = Column("site", String(255))
    description = Column("description", String(255), nullable=False)
    preferredSupplier = Column("preferred_supplier", Boolean, nullable=False, default=False)

    def __init__(self, name, cnpj, location, representative, phoneNumber, email, site, description):
        self.name = name
        self.cnpj = cnpj
        self.location = location
        self.representative = representative
        self.phoneNumber = phoneNumber
        self.email = email
        self.site = site
        self.description = description