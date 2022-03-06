start:
	poetry run task start

migrate:
	poetry run task migrate

seed:
	poetry run task seed

transfer:
	poetry run task transfer

credential:
	poetry run task credential

lint:
	poetry run pysen run lint

format:
	poetry run pysen run format

lint-fix:
	poetry run pysen run format && \
	poetry run pysen run lint

test:
	poetry run pytest

install-dev:
	poetry install

install:
	poetry install --no-dev
