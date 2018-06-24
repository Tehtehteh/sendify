FROM python:alpine

MAINTAINER Sergey Vlakh <tehfvpr@gmail.com>

COPY . /sendify

WORKDIR /sendify


RUN ["echo", "Installing dependencies..."]

RUN ["pip", "install", "-r", "requirements.txt"]

RUN ["echo", "Done installing dependencies. Launching application..."]

EXPOSE 8080

ENV PYTHONPATH="$PYTHONPATH:/sendify/src"

RUN ["echo", "Running tests..."]

RUN ["python", "src/tests/tests_main.py"]

RUN ["echo", "Launching application"]

CMD ["python", "src/main.py"]