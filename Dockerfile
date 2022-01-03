FROM python:3.8


WORKDIR /ayimforum

COPY Pipfile* /ayimforum/ 

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

COPY . /ayimforum/ 

EXPOSE 8000 

