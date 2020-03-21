install:
	pipenv install

run:
	pipenv run uvicorn main:app --reload

test:
	pipenv run pytest

test-coverage:
	pipenv run coverage run -m pytest
	pipenv run coverage report