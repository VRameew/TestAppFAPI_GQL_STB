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
class DeleteUserMutationType:
    msg: str
    error: str


class DeleteException(Exception):
    pass


@strawberry.type
class UpdateUserMutationType:
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

    @strawberry.mutation
    async def deleteUser(self, id: str) -> DeleteUserMutationType:
        try:
            print("Старт удаления")
            user = User.delete(id=id)
            if user:
                print()
                return DeleteUserMutationType(msg=f"Ползователь с id:{id} удален!", error='None')
            else:
                raise DeleteException('Не найден по ID')
        except Exception as e:
            return DeleteUserMutationType(msg='None', error=f"Error: {str(e)}")

    @strawberry.mutation
    async def updateUser(self, id: str, username: str, email: str, password_hash: str) -> UpdateUserMutationType:
        try:
            user = User.updete(id=id,username=username,
                               email=email, password_hash=password_hash)
            if user:
                return UpdateUserMutationType(data=user, error='None')
            else:
                return UpdateUserMutationType(data=None, error=f"User with id {id} not found")
        except Exception as e:
            return UpdateUserMutationType(data=None, error=f"Error: {str(e)}")


schema = strawberry.Schema(query=Query, mutation=Mutation)
