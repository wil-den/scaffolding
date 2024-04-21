#!make
.ONESHELL:

.PHONY: update
.PHONY: run
.PHONY: build
.PHONY: install

update:
	. venv/bin/activate
	which pip
	pip freeze > requirements.txt

run:	
	. venv/bin/activate;
	flask run;

build:
	. venv/bin/activate;
	python3 -m build;

install:
	python3 -m venv venv;
	. venv/bin/activate;
	python3 -m pip install --upgrade pip setuptools;
	pip install -r requirements.txt;



