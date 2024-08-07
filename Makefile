start:
	poetry run gunicorn -w 5 -b 0.0.0.0:8000 task_manager.wsgi

dev:
	poetry run python3 manage.py runserver 8080

install:
	poetry install

test:
	poetry run python manage.py test
	poetry run flake8

lint:
	poetry run flake8

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

compilemessages:
	poetry run django-admin compilemessages --ignore=.venv

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report