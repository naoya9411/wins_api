FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt