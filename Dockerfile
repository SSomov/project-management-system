FROM python:3.10-alpine
RUN pip install -U pip
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false
WORKDIR /code
COPY . /code/
RUN apk add --no-cache \
    curl \
    gcc \
    libressl-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libffi-dev && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH" && \
    poetry install --no-dev && \
    apk del \
        curl \
        gcc \
        libressl-dev \
        jpeg-dev \
        zlib-dev \
        musl-dev \
        libffi-dev