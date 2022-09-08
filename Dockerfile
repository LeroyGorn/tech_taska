FROM python:3.10

RUN apt update

RUN mkdir /tech_task

WORKDIR /tech_task

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./main.py ./main.py
COPY ./src ./src
