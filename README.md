# learn-hub

learnHUB official repository

## How to install ?

## Project onboarding

The learnHUB project is RESTful. The backend part is written in django v3+
(Python v3.8+), and the frontend part in React.JS (v16+)

### core folder

`core` folder contains the backend application (which is the django app).

#### How to add new dependencies ?

Add the new dependency into `requirements.in` (you could use `pip freeze`), then run `pip-compile --output-file=requirements.txt requirements.in`

### ui folder

`ui` folder contains the frontent part of the application (the react app).
