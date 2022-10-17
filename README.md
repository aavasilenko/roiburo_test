# roi-buro-test-project

## Name
ROI BURO sample test project

## Description
This is Django-based sample test project which collect information about CPU usage and shows this stats at HTML page.
There are client - linux daemon written on Python, which measures CPU utilization periodically and server - django application, which receives measures via REST API.

## Usage

```sh
pip install pipenv
cd src/server
pipenv install
cp app/env/env.sample app/env/env  # default environment variables
mkdir log
```

```sh
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

```sh
cd src/client
pipenv install
pipenv run python main.py
```

Visit http://127.0.0.1:8000/api/v1/core/system-state-details to view statistics

## Features

-   Django 3.2
-   Python 3.9
-   [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
-   Optimized settings
-   OpenAPI based docs via [drf-spectacular](https://github.com/tfranzel/drf-spectacular)