FROM python:3.10-slim-bullseye

WORKDIR /usr/src/app

COPY ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./server ./server

CMD ["./server/start_server.sh"]
