# Test-Driven Development with FastAPI and Docker

![Continuous Integration and Delivery](https://github.com/DerevenetsArtyom/fastapi-tdd/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

* https://secret-dusk-86918.herokuapp.com/docs
* https://secret-dusk-86918.herokuapp.com/summaries/
* https://secret-dusk-86918.herokuapp.com/summaries/4/

## Table of contents
- [About](#about)
  - [Objectives achieved in the project](#objectives-achieved-in-the-project)
  - [Tools and technologies](#tools-and-technologies)
  - [Endpoints](#endpoints)
- [Usage](#usage)
- [Tests](#tests)

## About

**fastapi-tdd** is a code-along (with some differences) to the course **[Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/)** by Michael Herman.
Link to [original repo](https://github.com/testdrivenio/fastapi-tdd-docker).

### Objectives achieved in the project

- Develop an asynchronous RESTful API with Python and FastAPI
- Practice Test-Driven Development
- Test a FastAPI app with pytest
- Interact with a Postgres database asynchronously
- Containerize FastAPI and Postgres inside a Docker container
- Run unit and integration tests with code coverage inside a Docker container
- Check the code for any code quality issues via a linter
- Configure GitHub Actions for continuous integration and deployment
- Use GitHub Packages to store Docker Images
- Speed up a Docker-based CI build with Docker Cache
- Deploy FastAPI, Uvicorn, and Postgres to Heroku with Docker
- Parameterize test functions and mock functionality in tests with pytest
- Run tests in parallel with pytest-xdist
- Document a RESTful API with Swagger/OpenAPI (out of the box)
- Run a background process outside the request/response flow

### Tools and technologies

This project uses a variety of technologies and services:
* **Core**
    - [Python](https://www.python.org/downloads/release/python-390/)
    - [FastAPI](https://fastapi.tiangolo.com/)
    - [Docker](https://www.docker.com/)
    - [Docker Compose](https://docs.docker.com/compose/)
    - [Postgres](https://www.postgresql.org/)
    - [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)
    - [Aerich](https://github.com/tortoise/aerich)
    - [Uvicorn](https://www.uvicorn.org/)
    - [Gunicorn](https://gunicorn.org/)
    - [Swagger/OpenAPI](https://swagger.io/docs/specification/about/)

* **Testing and Linting**
    - [Pytest](https://docs.pytest.org/en/6.2.x/)
    - [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)
    - [Flake8](https://gitlab.com/pycqa/flake8)
    - [Black](https://black.readthedocs.io/en/stable/)
    - [isort](https://isort.readthedocs.io/en/latest/)
    - [HTTPie](https://httpie.io/)

* **Services**
    - [GitHub Actions](https://github.com/features/actions)
    - [GitHub Packages](https://github.com/features/packages)
    - [Heroku](https://dashboard.heroku.com/)

### Endpoints

| Endpoint         | HTTP Method     | CRUD Method     | Result               |
|------------------|-----------------|-----------------|----------------------|
| `/summaries`     | **GET**         | **READ**        | get all summaries    |
| `/summaries/:id` | **GET**         | **READ**        | get a single summary |
| `/summaries`     | **POST**        | **CREATE**      | add a summary        |
| `/summaries/:id` | **PUT**         | **UPDATE**      | update a summary     |
| `/summaries/:id` | **DELETE**      | **DELETE**      | delete a summary     |
| `/ping`          | **GET**         |     ------      | get test json        |
| `/docs`          | **GET**         |     ------      | get the docs         |
