# drf-boilerplate
Simple DRF based boilerplate for quick bootstrapping of API applications.

# Contents
This project contains base skeleton of application based on the DRF/Django/Postgres.

It can be used as standalone API, backend for single-page or mobile app.

# Installation
1. Clone this repository and change current directory to its root
2. Create virtualenv: `python3.7 -m venv --prompt="(drf)" venv`
3. Activate it: `source venv/bin/activate`
4. Install requirements: `pip install -r ./requirements/base.txt`
5. Create user and database. I'm assuming that you'll use Postgres for this.
6. Run migrations: `python manage.py migrate`
7. Run server: `python manage.py runserver`
8. Open your browser at `http://localhost:8000`
