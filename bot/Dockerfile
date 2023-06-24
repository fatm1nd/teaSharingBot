FROM python:latest


COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

ADD main.py /bot/

WORKDIR /bot
