from fastapi import HTTPException

from app.repositories.user_repository import UserRepository
from app.repositories.refresh_token_repository import RefreshTokenRepository

from app.core.hashing import hash_password, verify_password
from app.services.email_service import EmailService
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    create_email_verification_token,
    create_password_reset_token
)


class AuthService:

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

        user_data["is_verified"] = False
        user_data["role"] = "user"

        await UserRepository.create_user(user_data)

        verification_token = create_email_verification_token(
            {
                "sub": user.email
            }
        )

        verification_link = (
            f"http://localhost:8000/verify-email?token={verification_token}"
        )

        EmailService.send_verification_email(
            user.email,
            verification_link
        )

        return {
            "message": "Registration successful. Please verify your email."
        }

    @staticmethod
    async def login(email: str, password: str):

        existing_user = await UserRepository.get_user_by_email(email)

        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        if not verify_password(
            password,
            existing_user["password"]
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid password"
            )

        if not existing_user["is_verified"]:
            raise HTTPException(
                status_code=403,
                detail="Please verify your email before logging in."
            )

        access_token = create_access_token(
            {
                "sub": existing_user["email"]
            }
        )

        refresh_token, jti, expire = create_refresh_token(
            {
                "sub": existing_user["email"]
            }
        )

        print("Generated JTI:", jti)

        await RefreshTokenRepository.create_refresh_token(
            {
                "user_email": existing_user["email"],
                "jti": jti,
                "expires_at": expire
            }
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    @staticmethod
    async def verify_email(token: str):

        payload = decode_token(token)

        if payload is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Verification Token"
            )

        if payload.get("type") != "email_verification":
            raise HTTPException(
                status_code=401,
                detail="Invalid Token Type"
            )

        email = payload.get("sub")

        existing_user = await UserRepository.get_user_by_email(
            email
        )

        if existing_user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        await UserRepository.verify_user(email)

        return {
            "message": "Email Verified Successfully"
        }

    @staticmethod
    async def refresh_access_token(refresh_token: str):

        print("========== REFRESH TOKEN ==========")

        payload = decode_token(refresh_token)

        print("Payload:", payload)

        if payload is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Refresh Token"
            )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=401,
                detail="Invalid Token Type"
            )

        email = payload.get("sub")
        jti = payload.get("jti")

        print("Email:", email)
        print("JTI:", jti)

        stored_token = await RefreshTokenRepository.get_refresh_token(
            jti
        )

        print("Stored Token:", stored_token)

        if stored_token is None:
            raise HTTPException(
                status_code=401,
                detail="Refresh Token Revoked"
            )

        existing_user = await UserRepository.get_user_by_email(email)

        if existing_user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        access_token = create_access_token(
            {
                "sub": existing_user["email"]
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    @staticmethod
    async def logout(refresh_token: str):

        # Step 1: Decode Refresh Token
        payload = decode_token(refresh_token)

        if payload is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Refresh Token"
            )

        # Step 2: Check Token Type
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=401,
                detail="Invalid Token Type"
            )

        # Step 3: Extract JTI
        jti = payload.get("jti")

        # Step 4: Delete Refresh Token
        result = await RefreshTokenRepository.delete_refresh_token(
            jti
        )

        # Step 5: Check if anything was deleted
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Refresh Token not found"
            )

        return {
            "message": "Logout Successful"
        }

    @staticmethod
    async def forgot_password(email: str):

        existing_user = await UserRepository.get_user_by_email(email)

        if existing_user is None:
            return {
                "message": "If the email exists, a password reset link has been sent."
            }

        reset_token = create_password_reset_token(
            {
                "sub": existing_user["email"]
            }
        )

        reset_link = (
            f"http://localhost:8000/reset-password?token={reset_token}"
        )

        EmailService.send_password_reset_email(
            existing_user["email"],
            reset_link
        )

        return {
            "message": "If the email exists, a password reset link has been sent."
        }

    @staticmethod
    async def reset_password(
        token: str,
        new_password: str
    ):

        payload = decode_token(token)

        if payload is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or Expired Token"
            )

        if payload.get("type") != "password_reset":
            raise HTTPException(
                status_code=401,
                detail="Invalid Token Type"
            )

        email = payload.get("sub")

        existing_user = await UserRepository.get_user_by_email(
            email
        )

        if existing_user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        hashed_password = hash_password(
            new_password
        )

        await UserRepository.update_password(
            email,
            hashed_password
        )

        return {
            "message": "Password reset successfully"
        }