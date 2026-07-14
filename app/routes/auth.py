from fastapi import APIRouter, HTTPException,Query
from app.schemas.auth_schema import RegisterRequest,ProfileResponse, RefreshTokenRequest
from fastapi.security import OAuth2PasswordRequestForm
from app.repositories.user_repository import UserRepository
from app.core.hashing import hash_password,verify_password
from app.core.security import create_access_token
from app.services.auth_service import AuthService
from fastapi import Depends
from app.dependencies.auth_dependency import get_current_user
from app.dependencies.role_dependency import require_role
from app.schemas.token_schema import RefreshTokenRequest 
from app.schemas.password_schema import (
    ForgotPasswordRequest,
    ResetPasswordRequest
)
from app.dependencies.role_dependency import require_role

router = APIRouter()

@router.post("/register")
async def register(user: RegisterRequest):
    return await AuthService.register(user)



@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return await AuthService.login(
        form_data.username,
        form_data.password
    )

@router.get(
        "/profile",
        response_model=ProfileResponse
        )
async def profile(
    current_user=Depends(get_current_user)
):
    return {
        "message": "Profile fetched successfully",
        "name": current_user["name"],
        "email": current_user["email"]
    }
@router.get("/admin/dashboard")
async def admin_dashboard(

    current_user=Depends(
        require_role("admin")
    )

):

    return {

        "message": "Welcome Admin",

        "admin": current_user["name"]

    }
@router.post("/refresh-token")
async def refresh_token(
    request: RefreshTokenRequest
):

    return await AuthService.refresh_access_token(
        request.refresh_token
    )
@router.post("/logout")
async def logout(request: RefreshTokenRequest):

    return await AuthService.logout(
        request.refresh_token
    )
@router.get("/verify-email")
async def verify_email(
    token: str = Query(...)
):

    return await AuthService.verify_email(token)
@router.post("/frogot-password")
async def forgot_password(
    request: ForgotPasswordRequest
):
    return await AuthService.forgot_password(request.email)
@router.post("/reset-password")
async def reset_password(
    request: ResetPasswordRequest
):
    return await AuthService.reset_password(
        request.token,
        request.new_password
    )
