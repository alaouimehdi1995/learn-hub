FROM python:3.8-alpine


# Installing OS libs required for psycopg2 (postgres) in a temporary folder
RUN apk update && apk add libpq
RUN apk add --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev

# Preparing working directory
WORKDIR /usr/src/app/
COPY requirements.txt ./

# Installing dependencies
RUN pip install -r requirements.txt

# Deleting the temporary folder to reduce the image size (commented because when
# a new dependency is installed, the `pip-compile` fails to rebuild psycopg2
#RUN apk del --no-cache .build-deps

# Exposing the application default port
EXPOSE 8000
