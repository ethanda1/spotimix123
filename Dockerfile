# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD [ "gunicorn", "-w", "4", "app:app"]
