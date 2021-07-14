black:
	@black --line-length 120 --exclude "\.git|\.github|\env" src/

isort:
	@isort src/

flake:
	@flake8 --config src/.flake8


lint: black flake isort

testing:
	docker-compose run --rm web python -m pytest -s -l
