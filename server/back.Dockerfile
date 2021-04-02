# back.Dockerfile

FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /server/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt