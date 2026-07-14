from dotenv import load_dotenv
import os
load_dotenv()  #it loads the environment variables from a .env file into the system's environment variables


# Application Settings
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

# MongoDB Settings
MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
# JWT Settings
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)
REFRESH_TOKEN_EXPIRE_DAYS = int(
    os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7)
)
MAIL_USERNAME = os.getenv("MAIL_USERNAME")

MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

MAIL_SERVER = os.getenv("MAIL_SERVER")

MAIL_PORT = int(os.getenv("MAIL_PORT"))

MAIL_FROM = os.getenv("MAIL_FROM")

MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")