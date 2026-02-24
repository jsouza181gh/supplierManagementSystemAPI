from pydantic import BaseModel, EmailStr, HttpUrl, Field, field_validator
from uuid import UUID
import re

class SupplierSchema(BaseModel):
    name : str = Field(..., min_length=1, max_length=100)
    cnpj : str
    location : str = Field(..., min_length=1, max_length=255)
    representative : str = Field(..., min_length=1, max_length=100)
    phoneNumber : str
    email : EmailStr
    site : HttpUrl
    description : str = Field(..., min_length=1, max_length=255)
    itemIds : list[UUID] | None = None
    isPreferred : bool | None = None

    @field_validator("cnpj")
    @classmethod
    def validate_cnpj(cls, value):
        pattern = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
        if not re.match(pattern, value):
            raise ValueError("CNPJ must be in format 00.000.000/0000-00")
        return value

    @field_validator("phoneNumber")
    @classmethod
    def validate_phone(cls, value):
        pattern = r"^\d{2} \d{5}-\d{4}( / \d{2} \d{5}-\d{4})*$"
        if not re.match(pattern, value):
            raise ValueError("Phone must be in format 00 00000-0000")
        return value