#### Base image ############################################
FROM python:3.8-alpine as base


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



#### Local image ###########################################
#  Has dev tools installed for local debugging and testing
FROM base as local

# Installing test requirements
COPY dev-requirements.txt ./
RUN pip install -r dev-requirements.txt



#### CI Image ##############################################
# The image copies all project files inside the container, and installs dev dependencies.
FROM local as CI

# Deleting the temporary folder to reduce the image size
RUN apk del --no-cache .build-deps

COPY . .



#### Production image ######################################
# The image copies all project files inside the container instead of using volumes
FROM base as production

# Deleting the temporary folder to reduce the image size
RUN apk del --no-cache .build-deps

COPY . .



# Exposing the application default port
EXPOSE 8000
