.PHONY: install lint docker-build docker-up docker-down dev-up dev-down logs ps

install:
	poetry install
	poetry run pre-commit install

lint:
	poetry run isort .
	poetry run ruff format .

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

dev-up:
	docker-compose up rabbitmq -d

dev-down:
	docker-compose stop rabbitmq

logs:
	docker-compose logs -f

ps:
	docker-compose ps
