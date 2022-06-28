.SHELLFLAGS: -ec

deps:
	@pipenv install

deps-dev:
	@pipenv install --dev 

help: deps
	@pipenv run python3 run.py --help

lint: deps-dev
	@pipenv run flake8

run-dev: deps
	@pipenv run python3 run.py --debug=True --reload=True

run: deps
	@pipenv run python3 run.py