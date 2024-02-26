FROM jupyter/all-spark-notebook:spark-3.5.0

WORKDIR /usr/src/app

COPY . .

COPY .env .env

RUN pip install --no-cache-dir -r requirements.txt

