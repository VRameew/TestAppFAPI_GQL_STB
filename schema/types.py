import strawberry
from typing import List, Union


@strawberry.type
class User:
    id: strawberry.ID
    username: str
    email: str


@strawberry.type
class ErrorMessage:
    message: str


@strawberry.type
class UserErrorMessage:
    data: User
    error: str


@strawberry.input
class CreateUserInput:
    username: str
    email: str
    password: str


@strawberry.type
class CreateUserMutationType:
    data: User
    error: str


@strawberry.type
class Query:
    @strawberry.field
    async def users(self) -> List[User]:
        pass

    @strawberry.field
    async def user(self, username: str) -> Union[User, ErrorMessage]:
        pass


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def createUser(self, input: CreateUserInput) -> CreateUserMutationType:
        pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
