FROM python:3.10-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY . .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
RUN chmod +x infrastructure/clean_code_check/start.sh

CMD ["./infrastructure/clean_code_check/start.sh"]


