# ************************************************
# install requirements
# ************************************************

.PHONY: install.prod
install.prod:
	pip install -r requirements.txt


install: install.prod  # install packages for local develop
	pip install -r requirements-local.txt


# ************************************************
# application
# ************************************************

.PHONY: run  # run the application in a dev mode
run:
	uvicorn src.main:app --host="0.0.0.0" --port=8080 --reload


.PHONY: deploy.prod  # deploy application to production
deploy.prod:
	echo "deploy using .env file"


# *************************************************
# code quality
# *************************************************

.PHONY: lint  # fix formatting / and order imports
lint:
	python -m isort .
	python -m black .
	python -m ruff --fix .


.PHONY: check  # check everything
check: lint
	python -m ruff check .
	python -m isort --check .
	python -m black --check .
	python -m mypy --check-untyped-defs src


# *************************************************
# tests
# *************************************************

.PHONY: test  # run all tests
test:
	python -m pytest -vvv -x ./src/tests
