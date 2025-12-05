from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated

database_url = "sqlite:///./database.db"
engine = create_engine(database_url)


def create_tables(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session() -> Session:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]