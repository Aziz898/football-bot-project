from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db/database.db')

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Модели таблиц

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    team_home = Column(String, nullable=False)
    team_away = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    status = Column(String, default='scheduled')
    score_home = Column(Integer, default=0)
    score_away = Column(Integer, default=0)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(String)
    published = Column(Boolean, default=False)

class Setting(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(Text)

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    time = Column(String)
    level = Column(String)
    message = Column(Text)

# Создание всех таблиц
def init_db():
    Base.metadata.create_all(bind=engine)
