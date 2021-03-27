from fastapi import FastAPI
from resources import user

app = FastAPI()


@app.get('/')
def index():
    return "Hello!!"


app.include_router(user.router)
