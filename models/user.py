from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String
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
    autoflush=False, expire_on_commit=False,)


# Функция для получения сессии
def get_session():
    try:
        session = SessionLocal()
        return session
    finally:
        session.close()


#Функция криптографии пароля
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
        return user
