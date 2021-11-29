from typing import Optional
from pydantic import BaseModel, EmailStr

# properties required for user creation


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
