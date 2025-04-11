FROM python:3.10.17-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"]

#docker run --gpus all -p 80:8000 fastapi