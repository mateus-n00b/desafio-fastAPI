from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    cpf: str
    nome: str
    data_nascimento: str
    cep: str
    rua: str
    bairro: str
    cidade: str
    estado: str


class UpdateUser(BaseModel):
    cpf: str
    nome: Optional[str] = None
    data_nascimento: Optional[str] = None
    cep: Optional[str] = None
    rua: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None