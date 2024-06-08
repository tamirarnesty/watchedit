SHELL := /bin/bash

install:
	@echo "Installing dependencies..."
	@pipenv install --dev

run:
	@echo "Running production server..."
	@pipenv run fastapi run src/main.py

dev:
	@echo "Running development server..."
	@pipenv run fastapi dev src/main.py
	