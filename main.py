from fastapi import FastAPI
from graphene import ObjectType, Schema, String, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = FastAPI()

# Настройка базы данных SQLAlchemy
engine = create_engine("postgres://user:password@postgres:5432/db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Модель SQLAlchemy
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password_hash = Column(String)


# Модель GraphQL
class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class Query(ObjectType):
    user = Field(UserType, username=String())
    users = List(UserType)

    def resolve_user(self, info, username):
        session = SessionLocal()
        return session.query(User).filter_by(username=username).first()

    def resolve_users(self, info):
        session = SessionLocal()
        return session.query(User).all()


# Маппинг модели
Base.metadata.create_all(bind=engine)


# Добавление GraphQL эндпоинта
schema = Schema(query=Query)
app.add_route("/graphql", schema)
