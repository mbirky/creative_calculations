export FLASK_APP=creative_calculations
export FLASK_ENV=development

all:
	@echo "make lint"
	@echo "    Run lint on project."
	@echo "make run"
	@echo "    Run the flask application"
	@echo "make test"
	@echo "    Run tests on project."

lint:
	pylint creative_calculations tests/* setup.py

run:
	flask run

test:
	pytest --cov