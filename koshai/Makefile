# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
DJANGO := $(PYTHON) manage.py
APP_NAME := your_app_name
PORT := 7000

# Targets
install:
	$(PIP) install -r requirements.txt

makemigrations:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

createsuperuser:
	$(DJANGO) createsuperuser

run:
	$(DJANGO) runserver $(PORT)

test:
	$(DJANGO) test $(APP_NAME)

shell:
	$(DJANGO) shell

collectstatic:
	$(DJANGO) collectstatic --noinput

pre-commit:
	pre-commit run --all-files

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf media/

.PHONY: install makemigrations migrate createsuperuser runserver test shell clean
