from typing import Union

from strawberry.tools import create_type

from models.user import User

CreateUserMutationType = create_type("CreateUserMutationType", User, (str,))
UpdateUserMutationType = create_type("UpdateUserMutationType", User, (str,))
DeleteUserMutationType = create_type("DeleteUserMutationType", str)


async def create_user(input) -> Union[CreateUserMutationType, str]:
    try:
        user = await User.create(**input)
        return CreateUserMutationType(user, None)
    except Exception as e:
        return CreateUserMutationType(None, f"Error: {str(e)}")


async def update_user(input) -> Union[UpdateUserMutationType, str]:
    try:
        user = await User.get(id=input.id)
        if user:
            await user.update_from_dict(input)
            return UpdateUserMutationType(user, None)
        else:
            return UpdateUserMutationType(None, "User not found")
    except Exception as e:
        return UpdateUserMutationType(None, f"Error: {str(e)}")


async def delete_user(input) -> Union[DeleteUserMutationType, str]:
    try:
        user = await User.get(id=input.id)
        if user:
            await user.delete()
            return DeleteUserMutationType("User deleted")
        else:
            return DeleteUserMutationType("User not found")
    except Exception as e:
        return DeleteUserMutationType(f"Error: {str(e)}")
