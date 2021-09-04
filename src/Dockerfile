# pull official base image
FROM python:3.9.7-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# add app
COPY app .

# add entrypoint.sh
COPY entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]