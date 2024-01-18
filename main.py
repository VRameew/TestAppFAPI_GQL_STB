from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema.types import schema
from models.user import Base, engine, get_session, User
import time


Base.metadata.create_all(bind=engine)
session = get_session()
print('Запрос')
users_list = session.query(User).all()
users_data = [user.__dict__ for user in users_list]
print(users_data)
print("Выход!!!!!!!!!!")
app = FastAPI()
app.add_route("/graphql", GraphQL(schema))
