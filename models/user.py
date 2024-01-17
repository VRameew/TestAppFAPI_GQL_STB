from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, String

Base = declarative_base()


# Модель SQLAlchemy
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password_hash = Column(String)

    def create(cls, session: Session, username: str, email: str, password: str) -> 'User':
        user = cls(username=username, email=email, password_hash=password)
        session.add(user)
        session.commit()
        return user


class UserModelInput:
    username: str
    email: str
    password: str
