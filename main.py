from fastapi import FastAPI
from models.user import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from strawberry.asgi import GraphQL
from schema.types import schema


app = FastAPI()
# Настройка базы данных SQLAlchemy
engine = create_engine("postgresql+psycopg2://user:password@postgres:5432/db",
                       echo=True, pool_pre_ping=True)
# Маппинг модели
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(
    binds={Base: engine}, autocommit=False,
    autoflush=False, expire_on_commit=False,)

#Будущий ендпоинт
app.add_route("/graphql", GraphQL(schema))
