export FLASK_APP=creative_calculations
export FLASK_ENV=development

all:
	@echo "make lint"
	@echo "    Run lint on project."
	@echo "make run"
	@echo "    Run the flask application"
	@echo "make setup"
	@echo "    Install the needed pips"
	@echo "make test"
	@echo "    Run tests on project."

lint:
	pipenv run pylint creative_calculations tests/* setup.py

run:
	pipenv run flask run

setup:
	pipenv install --dev

test:
	pipenv run pytest --cov
	pipenv run coverage xml