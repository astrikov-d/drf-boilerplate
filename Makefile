help:
	@echo "isort-check - check code by iSort"
	@echo "isort - iSorting all code"
	@echo "lint - run flake8 linter"
	@echo "test - run py.test with coverage plugin"

isort-check:
	isort -rc -c app
	isort -rc -c tests
	isort -rc -c conf
	isort -rc -c srv

isort:
	isort -rc app
	isort -rc tests
	isort -rc conf
	isort -rc srv

lint:
	flake8 app tests conf srv

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate
