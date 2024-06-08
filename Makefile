SHELL := /bin/bash

run-all:
	@echo "Running all services..."
	@docker compose watch

dev:
	@echo "Running all services in development..."
	@docker compose up --watch --build --force-recreate --remove-orphans
