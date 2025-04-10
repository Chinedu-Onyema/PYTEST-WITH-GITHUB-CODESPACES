# THIS FILE WILL KEEP ALL THE COMPLEX COMMANDS I WILL USE.
# IT IS LIKE A COOK BOOK GUIDE.

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greetings --cov=smath --cov=web tests
	python -m pytest --nbval notebook.ipynb

debug:
	python -m pytest -vv --pdb

lint:
	pylint --disable=R,C hello.py

format:
	black *.py

all: install lint test format