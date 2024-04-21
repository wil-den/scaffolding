#!make
.PHONY: update
.PHONY: run
.PHONY: build
.PHONY: install

update:
	. venv/bin/activate;
	pip freeze > requirements.txt;

run:	
	. venv/bin/activate;
	flask run;

build:
	. venv/bin/activate;
	python3 -m build;

install:
	python3 -m venv venv;
	. venv/bin/activate;
	pip install -r requirements.txt;



