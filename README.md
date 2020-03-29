# learn-hub project

[![Build Status](https://travis-ci.org/alaouimehdi1995/learn-hub.png?branch=master)](https://travis-ci.org/alaouimehdi1995/learn-hub)
[![codecov](https://codecov.io/gh/alaouimehdi1995/learn-hub/branch/master/graph/badge.svg)](https://codecov.io/gh/alaouimehdi1995/learn-hub)

## How to install ?

### Project requirements

In order to run (and contribute) to the project, you must have [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)(+v3.4)

### Installation steps

1. Clone the project with `git clone git@github.com:alaouimehdi1995/learn-hub.git` (or, if you intend to contribute, you should probably fork the project first then clone the forked version)
1. Build and run the project using `docker-compose up` (use `docker-compose up`)

That's it! Enjoy.

**Note:** The `docker-compose up` (or `docker-compose build`) are slow **only** the first time.

**Note 2:** You won't have to rebuild the images everytime you change the code. Only if the `docker-compose.yml` or one of `Dockerfiles` are updated

### Installation success

If the installation succeeds, you will be able to visit the following
addresses:

-   React app address: `http://localhost:3000/`
-   Django app address: `http://localhost:8000/admin/`

## Project technical details

If you intend to go further in the project (contribution, customization), or
even useful commands, please refer to the [contribution guide](/CONTRIBUTING.md)

In case you don't find your answer, don't hesitate to contact the project maintainer by email.
