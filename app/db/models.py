from sqlalchemy import Boolean, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, index=True, unique=True)
	email = Column(String, index=True, unique=True)
	full_name = Column(String, index=True)
	is_active = Column(Boolean, index=True, default=True)
	is_admin = Column(Boolean, index=True, default=False)
	hashed_password = Column(String)
