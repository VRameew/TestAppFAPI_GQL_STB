from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String
from typing import List, Optional
import uuid
import bcrypt

Base = declarative_base()
# Настройка базы данных SQLAlchemy
engine = create_engine("postgresql+psycopg2://user:password@postgres:5432/db",
                       echo=True, pool_pre_ping=True)
# Маппинг модели
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(
    binds={Base: engine}, autocommit=False,
    autoflush=False, expire_on_commit=False, )


# Функция для получения сессии
def get_session():
    session = SessionLocal()
    return session


# Функция криптографии пароля
def encrypt_text(text: str) -> str:
    encoded_text = text.encode('utf-8')
    hashed_text = bcrypt.hashpw(encoded_text, bcrypt.gensalt())
    return hashed_text.decode('utf-8')


# Модель SQLAlchemy
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password_hash = Column(String)

    def create(cls, username: str, email: str, password_hash: str) -> 'User':
        '''Метод класса User для создания данных в базе'''
        session = get_session()
        user = cls(id=uuid.uuid4(), username=username,
                   email=email, password_hash=encrypt_text(password_hash))
        session.add(user)
        session.commit()
        session.close()
        return user

    def delete(id: str) -> bool:
        '''Метод класса User для отбора данных по id и их удаление'''
        session = get_session()
        user = session.query(User).get(id)
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True
        return False

    def updete(id: str, username: str, email: str, password_hash: str) -> 'User':
        '''Метод класса User для изменения данных в базе'''
        session = get_session()
        user = session.query(User).get(id)
        if user:
            user.username = username
            user.email = email
            user.password_hash = encrypt_text(password_hash)
            session.commit()
            session.close()
        return user

    def listOfUsers(self) -> List['User']:
        '''Метод класса User для получения списка всех  данных в базе'''
        session = get_session()
        users_obj = session.query(User).all()
        users_list = [User(id=user.id, username=user.username, email=user.email) for user in users_obj]
        session.close()
        return users_list

    @staticmethod
    def userByUserName(username: str) -> Optional['User']:
        '''Метод класса User для получения по имени пользователя данных в базе'''
        session = get_session()
        user_obj = session.query(User).filter_by(username=username).first()
        session.close()
        return user_obj


