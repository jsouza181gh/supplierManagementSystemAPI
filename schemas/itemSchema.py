from pydantic import BaseModel, Field
from uuid import UUID

class ItemSchema(BaseModel):
    name : str = Field(..., min_length=1, max_length=100)
    category : str = Field(..., min_length=1, max_length=100)
    supplierIds : list[UUID] | None = None