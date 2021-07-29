black:
	@black --line-length 120 --exclude "\.git|\.github|\env" src/

isort:
	@isort src/

flake:
	@flake8 --config src/.flake8


lint: black flake isort

testing:
	docker-compose run --rm web python -m pytest -s -l

compile:
	@rm -f src/requirements*.txt
	@pip-compile src/requirements.in
	@pip-compile src/requirements-dev.in

sync:
	@pip-sync src/requirements*.txt

install: compile sync