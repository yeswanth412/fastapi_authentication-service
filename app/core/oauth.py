from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer( # is used to get the token from the request header
    tokenUrl="/login"
)