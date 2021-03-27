from fastapi import (APIRouter, HTTPException, Request)
from config.config import parse_configuration
from controller.bases.user import (User, UpdateUser)
from controller.database import DatabaseController

config = parse_configuration()

router = APIRouter()

db = DatabaseController(config['postgresql'])


@router.get('/users/user/', status_code=200)
def consulta_user(cpf: str):
    if not cpf:
        return HTTPException(
            400,
            "User is null"
        )
    return db.get_user(cpf)


@router.get('/users/', status_code=200)
def get_users():
    return db.get_users()


@router.post('/users/user/', status_code=201)
def insert_user(user: User):
    success = db.add_user(user)
    if not success:
        return HTTPException(
            500,
            "Error on creating user"
        )
    return "User created"


@router.put("/users/user/")
def update_user(user: UpdateUser):
    success = db.update_user(user)
    if not success:
        return HTTPException(
            500,
            "Error on updating user"
        )
    return "User created"


@router.delete("/users/user/")
def remove_user(cpf: str):
    success = db.delete_user(cpf)
    if not success:
        return HTTPException(
            500,
            "Error on updating user"
        )
    return "User deleted"
