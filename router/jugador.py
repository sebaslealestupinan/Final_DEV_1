from fastapi import APIRouter, HTTPException
from database import SessionDep
from models import JugadorPersonal, JugadorCreate

router = APIRouter()

@router.post("/", response_model=JugadorPersonal, status_code=201)
async def create_user(new_jugador:JugadorCreate, session:SessionDep):
    jugador = JugadorPersonal.model_validate(new_jugador)
    session.add(jugador)
    session.commit()
    session.refresh(jugador)
    return jugador


@router.get("/{jugador_numcam}", response_model=JugadorPersonal)
async def get_one_jugador(jugador_numcam:int, session:SessionDep):
    jugador_db = session.get(JugadorPersonal, jugador_numcam )
    if not jugador_db:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return jugador_db


@router.get("/", response_model=list[JugadorPersonal])
async def get_all_jugadores(session:SessionDep):
    users = session.query(JugadorPersonal).all()
    return users