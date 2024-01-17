import strawberry
from main import SessionLocal
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
    async def createUser(input: CreateUserInput) -> CreateUserMutationType:
        print("{:=^40}".format("Функция вызвана"))
        try:
            print("{:=^40}".format("try"))
            session = SessionLocal()
            user = await User.create(session, **input)
            session.commit()
            session.close()
            print("{:=^40}".format("second try"))
            print(user)
            return CreateUserMutationType(data=user, error=None)
        except Exception as e:
            print("{:=^40}".format("Exception"))
            print(e)
            return CreateUserMutationType(data=None, error=f"Error: {str(e)}")


schema = strawberry.Schema(query=Query, mutation=Mutation)
