import strawberry
from models.user import User
from typing import List, Union


@strawberry.type
class UserType:
    id: str
    username: str
    email: str


@strawberry.type
class ErrorMessage:
    message: str


@strawberry.type
class CreateUserMutationType:
    data: UserType
    error: str


@strawberry.type
class Query:
    @strawberry.field
    async def users(self) -> List[UserType]:
        pass

    @strawberry.field
    async def user(self, username: str) -> Union[UserType, ErrorMessage]:
        pass


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def createUser(self, username: str, email: str, password_hash: str) -> CreateUserMutationType:
        try:
            user = User.create(cls=User, username=username,
                               email=email, password_hash=password_hash)
            return CreateUserMutationType(data=user, error='None')
        except Exception as e:
            return CreateUserMutationType(data=None, error=f"Error: {str(e)}")


schema = strawberry.Schema(query=Query, mutation=Mutation)
