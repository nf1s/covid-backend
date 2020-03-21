install:
	pipenv install

run:
	pipenv run python main.py

test:
	pipenv run pytest

test-coverage:
	pipenv run coverage run -m pytest
