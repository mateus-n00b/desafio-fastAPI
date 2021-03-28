# FastAPI challenge

Autor: Mateus Sousa

Uma aplicação simples que demonstra o poder do _framework_ [FastAPI](https://fastapi.tiangolo.com/).

## Features
- [x] FastAPI
- [x] Postgres
- [x] Validacao de CPF
- [] uso JWT
- [x] Execução via Docker

## How to
Execute a aplicação através do comando [docker-compose](https://docs.docker.com/compose/install/):
``` docker-compose up ``

Em seguida, sinta-se à vontade para testar utilizando os _endpoints_ mapeados em docs/.
Importe a collection para o [Postman](https://www.postman.com/downloads/) e pronto!!

Devido a um um atraso de inicialização do container postgres, talvez a API não responda na primeira vez.
Sendo assim, cancele a execuçao e rode novamente o comando acima.

*PS: lembre-se de alterar o CPF nas requisições*


## TODO
- Validar data de nascimento com base no CPF
- Validar cep ao atualizar
- Documentar o bendito código
- Criar pacote Helm da API


