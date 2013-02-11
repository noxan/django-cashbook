VIRTUALENV=env

environment:
	test -d "$(VIRTUALENV)" || virtualenv --no-site-packages $(VIRTUALENV)

requirements: environment
	$(VIRTUALENV)/bin/pip install -r requirements.txt

server:
	$(VIRTUALENV)/bin/python manage.py runserver 0.0.0.0:8000
