from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dynaconf import settings


SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI
CONNECT_ARGS = {"check_same_thread": False}

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args=CONNECT_ARGS)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

