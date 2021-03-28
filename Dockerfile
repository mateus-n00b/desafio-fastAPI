FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD uvicorn --host 0.0.0.0 --port 8080 --reload main:app