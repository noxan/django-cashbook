VIRTUALENV=env

environment:
	test -d "$(VIRTUALENV)" || virtualenv --no-site-packages $(VIRTUALENV)

requirements: environment
	$(VIRTUALENV)/bin/pip install -r requirements.txt

runserver:
	$(VIRTUALENV)/bin/python manage.py runserver
