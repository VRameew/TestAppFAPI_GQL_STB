from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String
import uuid

Base = declarative_base()
# Настройка базы данных SQLAlchemy
engine = create_engine("postgresql+psycopg2://user:password@postgres:5432/db",
                       echo=True, pool_pre_ping=True)
# Маппинг модели
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(
    binds={Base: engine}, autocommit=False,
    autoflush=False, expire_on_commit=False,)


# Функция для получения сессии
def get_session():
    try:
        session = SessionLocal()
        return session
    finally:
        session.close()


# Модель SQLAlchemy
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password_hash = Column(String)

    def create(cls, username: str, email: str, password_hash: str) -> 'User':
        print("{:=^40}".format("session"))
        session = get_session()
        print(session)
        print("{:=^40}".format("user"))
        user = cls(id=uuid.uuid4(), username=username,
                   email=email, password_hash=password_hash)
        print(user)
        print("{:=^40}".format("session.add(user)"))
        session.add(user)
        print("{:=^40}".format("session.commit()"))
        session.commit()
        return user
