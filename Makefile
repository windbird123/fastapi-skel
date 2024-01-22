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

.PHONY: fmt  # fix formatting / and order imports
fmt:
	python -m black .
	python -m isort .


.PHONY: type  # check type annotations
type:
	python -m mypy --check-untyped-defs .


.PHONY: check  # check everything
check:
	python -m ruff .
	python -m black --check .
	python -m isort --check .
	python -m mypy --check-untyped-defs .
	python -m pytest .


# *************************************************
# tests
# *************************************************

.PHONY: test  # run all tests
test:
	python -m pytest -vvv -x ./src/tests

