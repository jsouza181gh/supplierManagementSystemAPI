from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class LoginSchema(BaseModel):
    email : EmailStr
    password : str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Must contain uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Must contain lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Must contain number")
        if not re.search(r"[@$!%*?&]", value):
            raise ValueError("Must contain special character")

        return value

class UserSchema(BaseModel):
    name : str = Field(..., min_length=1, max_length=100)
    lastName : str = Field(..., min_length=1, max_length=100)
    email : EmailStr
    password : str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Must contain uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Must contain lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Must contain number")
        if not re.search(r"[@$!%*?&]", value):
            raise ValueError("Must contain special character")

        return value