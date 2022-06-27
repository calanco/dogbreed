.SHELLFLAGS: -ec

deps:
	@pipenv install

deps-dev:
	@pipenv install --dev 

help: deps
	@pipenv run python3 run.py --help

lint: deps-dev
	@pipenv run flake8

run-debug: deps
	@pipenv run python3 run.py --debug=True

run: deps
	@pipenv run python3 run.py