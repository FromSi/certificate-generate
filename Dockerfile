FROM --platform=linux/amd64 python:3.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

CMD [ "python", "main.py" ]
