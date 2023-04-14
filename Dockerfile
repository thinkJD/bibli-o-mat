FROM python:3.11-slim as base

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

FROM base as release

COPY src/* /usr/app/

ENTRYPOINT [ "/usr/app/bibli-o-mat.py" ]

