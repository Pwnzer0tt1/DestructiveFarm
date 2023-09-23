FROM python:3.10-slim-bullseye

WORKDIR /app/server

RUN apt-get update
RUN apt-get install build-essential python3-dev

ADD ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./server ./
ENV FLASK_APP=/app/server/standalone.py
WORKDIR /app
ADD ./run.py ./

CMD ["python3", "run.py"]
 
