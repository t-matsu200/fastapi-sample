FROM python:3.9

ENV PIP_DEFAULT_TIMEOUT 1000

WORKDIR /app

RUN apt update && \
    apt install -y python3-dev default-mysql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080