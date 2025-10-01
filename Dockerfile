FROM python:3.12.11-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY main.py /app

EXPOSE 9098

CMD ["python3", "main.py"]