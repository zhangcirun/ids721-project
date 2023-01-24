install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black project1/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py project1/*.py

all: install format lint