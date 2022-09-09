FROM python:3.10-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY . .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

RUN --mount=type=cache,target=/root/.cache \
    pip install -e PNLU/entity_recognizer
RUN --mount=type=cache,target=/root/.cache \
    pip install -e PNLU/utilities

CMD [ "pytest"]

