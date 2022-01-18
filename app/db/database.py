from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = "sqlite:///./app/db/db.sqlite3" # Local
# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL'].replace("://", "ql://", 1) # Heroku

engine = create_engine(SQLALCHEMY_DATABASE_URL,
	connect_args={'check_same_thread': False}) # SQLite

# engine = create_engine(SQLALCHEMY_DATABASE_URL) # PostgreSQL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
