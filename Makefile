.PHONY: install lint

install:
	poetry install
	poetry run pre-commit install

lint:
	poetry run isort .
	poetry run ruff format .
