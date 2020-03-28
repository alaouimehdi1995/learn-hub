# learn-hub project

[![Build Status](https://travis-ci.org/alaouimehdi1995/learn-hub.png?branch=master)](https://travis-ci.org/alaouimehdi1995/learn-hub)
[![codecov](https://codecov.io/gh/alaouimehdi1995/learn-hub/branch/master/graph/badge.svg)](https://codecov.io/gh/alaouimehdi1995/learn-hub)

## 1. How to install ?

### 1.1 Project requirements

In order to run (and contribute) to the project, you must have [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)(+v3.4)

### 1.2 Installation steps

1. Clone the project with `git clone git@github.com:alaouimehdi1995/learn-hub.git` (or, if you intend to contribute, you should probably fork the project first then clone the forked version)
1. Build and run the project using `docker-compose up` (use `docker-compose up`)

That's it! Enjoy.
**Note:** The `docker-compose up` (or `docker-compose build`) are slow **only** the first time.
**Note 2:** You won't have to rebuild the images everytime you change the code. Only if update the `docker-compose.yml` or one of `Dockerfiles`

### 1.3 Useful adresses

-   React app address: `http://localhost:3000/`
-   Django app address: `http://localhost:8000/`

## 2. Project onboarding

### 2.1 Useful commands

-   `docker-compose up` to run (and build if not already built) the project
-   `docker-compose up -d` Same as the previous, but the app is run in the background (no showing logs)
-   `docker-compose exec [service_name] [command]` to execute a custom command inside on of the existing services: `postgresql_db`(database), `web-server`(django app), `ui`(react app)

Example: if you want to run migrations for the django app: `docker-compose exec web-server python manage.py migrate` (`sh` as command instead if you want to run a shell)

-   `docker-compose stop` to stop your services
-   `docker-compose build` to force the build (for example if you changed the `docker-compose.yml` or one of the `Dockerfiles`)

### 2.2 Project stack

The project is RESTful. Here are the technologies used:

-   Reactjs (v16.13) for the frontend part. Note that we use typescript for better type hinting.
-   Django v3.0 (Python v3.8) for the backend.
-   PostgreSQL (v12.2) for the database.
-   Docker and docker-compose for the application's containerization.

### 2.3 Project structure

-   `core/` folder contains the backend (django app)
-   `ui/` folder contains the react application

### 2.4 How to add new dependencies ?

Note: For installing dependencies, your application should be up (`docker-compose up`)

#### For django application

In order to include a new python dependency to the project, here are the steps to follow:

1. Access to your container's shell using the `docker-compose exec web-server sh` command
1. Install your new dependency (inside the container) with `pip install [YOUR_PACKAGE_NAME]`
1. Save your virtual env dependencies in the `.in` file using: `pip freeze > requirements.in`
1. Re-generate the `requirements.txt` file with: `pip-compile --output-file=requirements.txt requirements.in`
1. Stop your app and rebuild the docker images (`docker-compose stop && docker-compose build`)
1. Re-run your app (`docker-compose up`)

Then, once satisfied, save your changes (`git add requirements.in requirements.txt`) then commit them

#### For react application

In order to include a new JS dependency to the project, here are the steps to follow:

1. Access to your container's shell using the `docker-compose exec ui sh` command
1. Install your new package with `npm install [options] [your_package_name]`
1. Stop your app and rebuild the docker images (`docker-compose stop && docker-compose build`)
1. Re-run your app (`docker-compose up`)

Then, once satisfied, save your changes (`git add package.json package-lock.json`) then commit them
