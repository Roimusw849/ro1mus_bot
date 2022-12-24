FROM python:alpine

WORKDIR /bot

RUN pip install aiogram
RUN pip install requests

COPY . .

CMD [ "python", "main.py" ]
