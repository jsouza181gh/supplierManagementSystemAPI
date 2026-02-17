from pydantic import BaseModel, Field
from uuid import UUID

class DocumentSchema(BaseModel):
    name : str = Field(..., min_length=1, max_length=100)
    path : str  = Field(..., min_length=1, max_length=255)
    category : str  = Field(..., min_length=1, max_length=100)
    supplierId : UUID | None = None