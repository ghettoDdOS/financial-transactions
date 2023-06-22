.PHONY: run-server
run-server:
	poetry run python ./manage.py runserver localhost:8080

.PHONY: run-client
run-client:
	yarn dev --host localhost --port 8000 --https

.PHONY: run
run:
	@make -j 2 run-server run-client

.PHONY: install-server
install-server:
	poetry install

.PHONY: install-client
install-client:
	yarn install

.PHONY: init-dotenv
init-dotenv:
	copy .env.example .env || cp .env.example .env

.PHONY: install
install:
	@make init-dotenv
	@make -j 2 install-server install-client
