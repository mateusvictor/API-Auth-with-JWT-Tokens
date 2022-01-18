from sqlalchemy.orm import Session
from .db.models import User
from . import schemas
from .password import get_password_hash

	
def get_user_by_username(db: Session, username: str):
	return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
	return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session):
	return db.query(User).all()


def create_user(db: Session, user: schemas.UserCreate):
	user_dict = user.dict()
	hashed_password = get_password_hash(user_dict.pop('password'))

	db_user = User(**user_dict, hashed_password=hashed_password)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)

	return db_user


def delete_user(db: Session, user: User):
	db.delete(user)
	db.commit()
	return 