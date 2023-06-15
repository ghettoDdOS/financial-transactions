.PHONY: run-server
run-server:
	poetry run python ./manage.py runserver localhost:8080

.PHONY: run-client
run-client:
	yarn dev --host localhost --port 8000 --https

.PHONY: run
run:
	@make -j 2 run-server run-client
