FROM python:3.10-slim-bullseye

WORKDIR /usr/src/app

COPY ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./server ./server
RUN echo "from server import app" > start.py
CMD ["gunicorn", "--bind" ,"0.0.0.0:5000" , "start:app"]
