from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from utils.positions import Position
from utils.states import States


class JugadorPersonal(SQLModel, table=True):
    nombre: str
    numero_cam: int
    year: int
    image_url: Optional[str] = None
    nacionalidad:str

    partidos: List["Partido"] = Relationship(back_populates="jugador")

class JugadorDeportivo(SQLModel, table=True):
    altura: float
    peso: float
    pie_dominante: str
    posicion: Position
    year_ingreso_equipo: int
    estado: States


class Estadistica():
    total_tiempo: int
    goles_anotados: int
    faltas: int
    tarjetas: int



class Partido():
    fecha: str
    resultado: str


