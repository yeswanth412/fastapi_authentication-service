from fastapi import Depends, HTTPException, status

from app.core.oauth import oauth2_scheme

from app.core.security import verify_access_token

from app.repositories.user_repository import UserRepository
async def get_current_user(   #fastpi uses async function to get the current user from the token

    token: str = Depends(oauth2_scheme)

):

    payload = verify_access_token(token)  #verifies the token and returns the payload

    email = payload.get("sub")

    user = await UserRepository.get_user_by_email(email)   # repository function to get the user by email from the database mongodb

    # and we use the mongodb means database for the verification is there ay modification is been done between logind

    # and now if there are any changes occured it will match with the jwt

    if not user:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="User not found"

        )

    return user