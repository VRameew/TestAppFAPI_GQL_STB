from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema.types import schema
from models.user import Base, engine, get_session, User
import time


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_route("/graphql", GraphQL(schema))
