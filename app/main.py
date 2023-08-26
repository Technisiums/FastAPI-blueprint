from fastapi import FastAPI
from app.routers import auth, healthcheck, persons
from fastapi_sqlalchemy import DBSessionMiddleware
from app.config.settings import settings
app = FastAPI()
app.add_middleware(DBSessionMiddleware,db_url=settings.SQLALCHEMY_DATABASE_URI)

app.include_router(auth.router)
app.include_router(healthcheck.router)
app.include_router(persons.router)
