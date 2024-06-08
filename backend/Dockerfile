FROM python:3.12

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile* ./

# install dependencies
RUN pip install pipenv
RUN pipenv install

COPY --chown=src:src src/ ./src/

EXPOSE 8000

CMD [ "pipenv", "run", "fastapi", "run", "src/main.py" ]
