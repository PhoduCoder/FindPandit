FROM python:3.9-slim-buster

RUN mkdir /app

COPY app /app
COPY templates /app/templates
COPY requirements.txt /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
