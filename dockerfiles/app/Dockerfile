FROM python:alpine

MAINTAINER Sergey Vlakh <tehfvpr@gmail.com>

WORKDIR /sendify

RUN ["echo", "Installing dependencies..."]
RUN ["pip", "install", "-r", "requirements.txt"]



RUN ["echo", "Done installing dependencies. Launching application..."]

CMD ["python", "main.py"]