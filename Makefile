.PHONY: bootstrap
bootstrap:
	pip install poetry
	cp .env_example .env
	docker-compose up -d
	make install-dev
	poetry add greenlet --dev
	poetry run task migrate
	poetry run task seed

.PHONY: cleanup
cleanup:
	docker-compose down --rmi all --volumes --remove-orphans

.PHONY: start
start:
	poetry run task start

.PHONY: transfer
transfer:
	poetry run task transfer

.PHONY: credential
credential:
	poetry run task credential

.PHONY: lint
lint:
	poetry run pysen run lint

.PHONY: format
format:
	poetry run pysen run format

.PHONY: lint-fix
lint-fix:
	poetry run pysen run format && \
	poetry run pysen run lint

.PHONY: test
test:
	poetry run pytest

.PHONY: install-dev
install-dev:
	poetry install

.PHONY: install
install:
	poetry install --no-dev
