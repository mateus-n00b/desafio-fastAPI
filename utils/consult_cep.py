import requests as rq


def consult(cep: str) -> tuple:
    url_api = f"https://viacep.com.br/ws/{cep}/json/"
    response = rq.get(url_api)
    if response.json().get('erro'):
        return False, -1
    return True, response.json()
