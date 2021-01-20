FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

LABEL maintainer="Colin Chen <me@co1in.com>"

RUN pip install --no-cache-dir fastapi redis

COPY ./app /app