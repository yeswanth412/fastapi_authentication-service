from app.database.mongodb import database  #it imports from mongodb

class UserRepository:

    collection = database.get_collection("users")

    @classmethod
    async def get_user_by_email(cls,email:str):
        return await cls.collection.find_one({"email": email})  #get the user details from the database by matching email
    
    @classmethod
    async def create_user(cls, user_data: dict):
        return await cls.collection.insert_one(user_data)  #insert the new user details and store in the mongodb
    @staticmethod
    async def verify_user(email: str):

        return await UserRepository.collection.update_one(
        {
            "email": email
        },
        {
            "$set": {
                "is_verified": True
            }
        }
    )
    @staticmethod
    async def update_password(
    email: str,
    password: str
):

        return await UserRepository.collection.update_one(
        {
            "email": email
        },
        {
            "$set": {
                "password": password
            }
        }
    )