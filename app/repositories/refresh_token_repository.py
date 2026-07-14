from app.database.mongodb import database


class RefreshTokenRepository:

    collection = database["refresh_tokens"]

    @classmethod
    async def create_refresh_token(
        cls,
        token_data: dict
    ):
        return await cls.collection.insert_one(token_data)


    @classmethod
    async def get_refresh_token(
        cls,
        jti: str
    ):
        return await cls.collection.find_one(
            {
                "jti": jti
            }
        )


    @classmethod
    async def delete_refresh_token(
        cls,
        jti: str
    ):
        return await cls.collection.delete_one(
            {
                "jti": jti
            }
        )