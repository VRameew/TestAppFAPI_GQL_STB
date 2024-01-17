from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=200, unique=True)
    username = fields.CharField(max_length=200, unique=True, index=True)
    password_hash = fields.CharField(max_length=200)


class UserModelInput:
    username: str
    email: str
    password: str
