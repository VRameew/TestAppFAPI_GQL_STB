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


@strawberry.input
class CreateUserInput:
    username: str
    email: str
    password: str


@strawberry.input
class UpdateUserInput:
    id: strawberry.ID
    username: str
    email: str
    password: str


@strawberry.input
class DeleteUserInput:
    id: strawberry.ID


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
    async def create_user(self, input: CreateUserInput) -> Union[User, ErrorMessage]:
        pass

    @strawberry.mutation
    async def update_user(self, input: UpdateUserInput) -> Union[User, ErrorMessage]:
        pass

    @strawberry.mutation
    async def delete_user(self, input: DeleteUserInput) -> Union[ErrorMessage, None]:
        pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
