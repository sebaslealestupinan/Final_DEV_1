from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from utils.positions import Position
from utils.states import States


class JugadorBase(SQLModel):
    name: str | None = Field(description="User name")
    year: int | None = Field(description="User year")
    status: bool | None = Field(description="User status", default=True)

class Jugador(JugadorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    #nombre: str
    #year: int
    #numero_cam: int | None = Field(default=None, primary_key=True)
    #nacionalidad: str


class JugadorCreate(JugadorBase):
    pass
    #nombre:str
    #year:int
    #numero_cam:int
    #nacionalidad:str


