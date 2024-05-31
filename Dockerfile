# pull official base image
FROM python:3.12-slim-bullseye
RUN apt update
RUN apt install python3-dev default-libmysqlclient-dev build-essential pkg-config -y
RUN apt install netcat -y
# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

ENTRYPOINT ["sh","./entrypoint.sh"]
