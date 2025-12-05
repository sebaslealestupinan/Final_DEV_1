from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, Relationship, black_
from utils.positions import Position
from utils.states import States


class JugadorBase(SQLModel):
    name: str | None = Field(description="User name", index = True)
    year: int | None = Field(description="User year")
    status: bool | None = Field(description="User status", default=True)
    t-chirt_numero: int | None = Field(default=None, primary_key=True)
    state: str

class Jugador(JugadorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    : str

class Partido(SQLModel, table= True):
    id: int | None = Field(default = None, primary_key= True)
    t: str
    plantilla: Optional["jugadorPartido"] = Relationship(black_)