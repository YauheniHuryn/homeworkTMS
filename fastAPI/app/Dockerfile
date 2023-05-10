FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

EXPOSE 80

ADD requirements.txt /tmp/requirements.txt

RUN python -m pip install -r /tmp/requirements.txt

ARG version=0.0.0

COPY . /app
#RUN /app/src/__init__.py
ENV MODULE_NAME=src.main