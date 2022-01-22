FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

RUN apt install ca-certificates
COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    CURL_CA_BUNDLE="" && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD uvicorn --host=0.0.0.0 src.main:app