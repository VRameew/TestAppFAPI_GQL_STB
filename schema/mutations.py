from typing import Union

import strawberry

from models.user import User
from schema.types import CreateUserInput


@strawberry.type
class CreateUserMutationType:
    data: User
    error: str


@strawberry.mutation
async def createUser(input: CreateUserInput) -> CreateUserMutationType:
    try:
        user = await User.create(**input)
        return CreateUserMutationType(data=user, error=None)
    except Exception as e:
        return CreateUserMutationType(data=None, error=f"Error: {str(e)}")
