from fastapi import (APIRouter, HTTPException, Request)
from config.config import parse_configuration
from controller.bases.user import (User, UpdateUser)
from controller.database import DatabaseController
from utils.valid_cpf import validate
from utils.consult_cep import consult

config = parse_configuration()

router = APIRouter()

db = DatabaseController(config['postgresql'])
db.create_table()


@router.get('/users/user/', status_code=200)
def get_user(cpf: str):
    if not validate(cpf):
        return HTTPException(
            500,
            "Invalid CPF"
        )
    if not cpf:
        return HTTPException(
            400,
            "User is null"
        )
    data = db.get_user(cpf)
    if len(data) < 1:
        return HTTPException(
            404,
            "User not found"
        )
    return data


@router.get('/users/', status_code=200)
def get_users():
    return db.get_users()


@router.post('/users/user/', status_code=201)
def insert_user(user: User):
    if not validate(user.cpf):
        return HTTPException(
            500,
            "Invalid CPF"
        )

    cep_valid = consult(user.cep)
    cep_json = cep_valid[1]
    if not cep_valid[0]:
        return HTTPException(
            500,
            "Invalid CPF"
        )

    user.estado = cep_json.get('uf')
    user.cidade = cep_json.get('localidade')
    user.rua = cep_json.get('logradouro')

    success = db.add_user(user)
    if not success:
        return HTTPException(
            500,
            "Error on creating user"
        )
    return "User created"


@router.put("/users/user/")
def update_user(user: UpdateUser):
    if not validate(user.cpf):
        return HTTPException(
            500,
            "Invalid CPF"
        )

    if len(db.get_user(user.cpf)) < 1:
        return HTTPException(
            404,
            "User not found"
        )

    success = db.update_user(user)
    if not success:
        return HTTPException(
            500,
            "Error on updating user"
        )
    return "User updated"


@router.delete("/users/user/")
def remove_user(cpf: str):
    if not validate(cpf):
        return HTTPException(
            500,
            "Invalid CPF"
        )

    if len(db.get_user(cpf)) < 1:
        return HTTPException(
            404,
            "User not found"
        )

    success = db.delete_user(cpf)
    if not success:
        return HTTPException(
            500,
            "Error on updating user"
        )
    return "User deleted"
