FROM python:3.11-slim as base

RUN pip install poetry

RUN mkdir /usr/app
WORKDIR /usr/app

COPY . .
RUN poetry install --no-dev

ENTRYPOINT [ "poetry", "run", "bibli-o-mat" ]

CMD [ "--help" ]