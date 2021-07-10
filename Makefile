black:
	@black --line-length 120 --exclude "\.git|\.github|\env" .

isort:
	@isort .

flake:
	@flake8 .


lint: black flake isort