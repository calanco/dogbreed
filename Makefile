.SHELLFLAGS: -ec

PYTHON = pipenv run python3

deps-dev:
	@pipenv install --dev 

help: deps-dev
	@$(PYTHON) run.py --help

lint: deps-dev
	@pipenv run flake8

run-dev: deps-dev
	@$(PYTHON) run.py --debug=True --reload=True

build:
	@docker build -t dogbreed .

run: build
	@docker run -p 8080:8080 dogbreed:latest