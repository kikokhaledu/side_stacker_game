FROM python:3.10


ENV  PYTHONBUFFERED = 1


WORKDIR /app

ADD . .


RUN pip install -r requirments.txt
RUN python manage.py makemigrations

EXPOSE 8000