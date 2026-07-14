# a schema handles the incoming and outgoing data for the authentication endpoints
from pydantic import BaseModel, EmailStr,Field
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException
from app.core.hashing import (
    verify_password,
    hash_password
)
 
class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    role: str = "user"
class ProfileResponse(BaseModel):
    name: str
    email: EmailStr

@staticmethod
async def register(user):

    existing_user = await UserRepository.get_user_by_email(
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_data = user.model_dump()

    user_data["password"] = hash_password(
        user.password
    )

    await UserRepository.create_user(user_data)

    return {
        "message": "User Registered Successfully"
    }
class RefreshTokenRequest(BaseModel):
    refresh_token: str