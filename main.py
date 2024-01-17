from fastapi import FastAPI
from strawberry.asgi import GraphQL
from tortoise.contrib.fastapi import register_tortoise

from models.user import User
from schema.types import schema
from schema.mutations import create_user, update_user, delete_user


app = FastAPI()

app.add_route("/graphql",
              GraphQL(
                  schema,
                  mutation=[create_user,
                            update_user,
                            delete_user]))
register_tortoise(
    app,
    db_url="postgresql://user:password@postgres:5432/db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}
