.SHELLFLAGS: -ec

deps-dev:
	@pipenv install --dev 

help: deps-dev
	@pipenv run python3 run.py --help

lint: deps-dev
	@pipenv run flake8

run-dev: deps-dev
	@pipenv run uvicorn --host=0.0.0.0 --reload --debug app.main:app

build:
	@docker build -t dogbreed .

run: build
	@docker run -p 8080:8080 dogbreed:latest