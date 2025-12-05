from fastapi import APIRouter, HTTPException
from database import SessionDep
from models import JugadorPersonal, JugadorDeportivo, JugadorCreate

router = APIRouter()

@router.post("/", response_model=JugadorPersonal, status_code=201)
async def create_user(new_jugador:JugadorCreate, session:SessionDep):
    jugador = JugadorPersonal.model_validate(new_jugador)
    session.add(jugador)
    session.commit()
    session.refresh(jugador)
    return jugador

@router.get("/{user_id}", response_model=JugadorPersonal)
async def get_one_user(user_id:int, session:SessionDep):
    user_db = session.get(JugadorPersonal, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    return user_db


@router.get("/", response_model=list[JugadorPersonal])
async def get_all_users(session:SessionDep):
    users = session.query(JugadorPersonal).all()
    return users