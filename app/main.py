from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import models
from .db.database import SessionLocal, engine
from .routers import users


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
	title='Auth System',
	description='API designed to learn how authenticate a user with OAuth2'
				' system with JWT tokens.')

app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

app.include_router(users.router)

