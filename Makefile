.SHELLFLAGS: -ec

PYTHON = pipenv run python3

deps-dev:
	@pipenv install --dev 

help: deps-dev
	@$(PYTHON) run.py --help

lint: deps-dev
	@pipenv run pre-commit run --all-files

run-dev: deps-dev
	@export DB_HOSTNAME=localhost; \
	$(PYTHON) run.py --debug=True --reload=True

build:
	@docker build -t dogbreed .

run: build
	@docker run --rm -p 8080:8080 -e DB_HOSTNAME=host.docker.internal \
		dogbreed:latest

build-postgres:
	@docker build -t postgres-dogbreed data

run-db: build-postgres
	@docker run --rm -p 5432:5432 postgres-dogbreed:latest