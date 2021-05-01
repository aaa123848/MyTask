FROM python:3.8-alpine3.12
RUN apk add --no-cache tini
RUN apk upgrade --no-cache

WORKDIR /app
RUN python -m pip install pip==21.0.0
RUN pip install beautifulsoup4
RUN pip install requests

COPY . .
