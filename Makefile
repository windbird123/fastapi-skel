# ************************************************
# install requirements
# ************************************************

.PHONY: install.prod
install.prod:
	pip install -r requirements.txt


install: install.prod  # install packages for dev
	pip install -r requirements-dev.txt


# ************************************************
# application
# ************************************************

.PHONY: run.prod  # run the application in a prod mode
run.prod:
	uvicorn main:app --host="0.0.0.0" --port=8080


.PHONY: run  # run the application in a dev mode
run:
	uvicorn main:app --host="0.0.0.0" --port=8080 --reload


# *************************************************
# code quality
# *************************************************

.PHONY: format  # fix formatting / and order imports
format:
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

.PHONY: test.unit  # run unit tests
test.unit:
	python -m pytest -vvv -x ./src/tests/unit

.PHONY: test.integration  # run integration tests
test.integration:
	python -m pytest -vvv -x ./src/tests/integration
