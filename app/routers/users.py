from datetime import datetime, timedelta
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import User, UserCreate
from ..dependencies import get_db
from .. import crud
from ..dependencies import (
    get_current_active_user, 
    get_current_admin_user, 
    create_access_token,
    authenticate_user, 
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


router = APIRouter(
    tags=['users'])


@router.post('/token/')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)):

    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Incorrect username or password', 
            headers={'WWW-Authenticate': 'Bearer'})

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/users/', response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user


@router.get('/users/me/', response_model=User)
async def read_my_user(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.delete('/users/{user_id}/', response_model=[])
async def delete_user(user_id: int, db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_admin_user)):

    db_user = crud.get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid user ID')

    db_delete = crud.delete_user(db=db, user=db_user)
    return []


@router.get('/users/', response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db=db)
