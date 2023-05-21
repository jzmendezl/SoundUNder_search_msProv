FROM python:3.9-alpine3.13
LABEL maintainer="kamedinava@unal.edu.co"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./SoundUNder_search_ms /SoundUNder_search_ms

WORKDIR /SoundUNder_search_ms
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \ 
    build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps &&\
    adduser --disabled-password --no-create-home SoundUNder_search_ms

ENV PATH="/py/bin:$PATH"

USER SoundUNder_search_ms




