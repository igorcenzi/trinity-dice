FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt --upgrade-pip

WORKDIR /app

COPY . /app/