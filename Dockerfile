FROM python:alpine

MAINTAINER Sergey Vlakh <tehfvpr@gmail.com>

COPY . /sendify

WORKDIR /sendify


RUN ["echo", "Installing dependencies..."]

RUN ["pip", "install", "-r", "requirements.txt"]

RUN ["echo", "Done installing dependencies. Launching application..."]

EXPOSE 8080

RUN ["export",  "PYTHONPATH=\"${PYTHONPATH}:/sendify/src\""]
RUN ["echo", "$PYTHONPATH"]

CMD ["python", "src/main.py"]