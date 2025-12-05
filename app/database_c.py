from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated

database_url = "sqlite:///./database.db"
engine = create_engine(database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]