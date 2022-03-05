start:
	poetry run tasks start

migrate:
	poetry run tasks migrate

seed:
	poetry run tasks seed

transfer:
	poetry run tasks transfer

credential:
	poetry run tasks credential

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
