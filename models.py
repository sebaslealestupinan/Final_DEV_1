from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Jugador():
    nombre: str
    numero_cam: int
    year: int
    nacionalidad:str


class Estadistica():
    pass


class Partido():
    pass


