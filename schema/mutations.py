import strawberry

from schema.types import CreateUserInput


@strawberry.type
class CreateUserMutationType:
    data: User
    error: str


@strawberry.mutation
async def createUser(input: CreateUserInput) -> CreateUserMutationType:
    print("{:=^40}".format("Функция вызвана"))
    try:
        user = await User.create(**input)
        print(user)
        return CreateUserMutationType(data=user, error=None)
    except Exception as e:
        return CreateUserMutationType(data=None, error=f"Error: {str(e)}")
