from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema.types import schema
from models.user import Base, engine


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_route("/graphql", GraphQL(schema))
