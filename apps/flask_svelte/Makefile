.ONESHELL:

.PHONY: server-update
.PHONY: install-app
.PHONY: build
.PHONY: ui-build
.PHONY: ui-install
.PHONY: ui
.PHONY: server-install
.PHONY: server-build
.PHONY: server


server-update:
	cd server;
	. venv/bin/activate
	which pip
	pip freeze > requirements.txt

server:
	cd server;	
	. venv/bin/activate;
	flask run;

server-build:
	cd server;
	. venv/bin/activate;
	python3 -m build;

server-install:
	cd server;
	python3 -m venv venv;
	. venv/bin/activate;
	python3 -m pip install --upgrade pip setuptools;
	pip install -r requirements.txt;

ui:
	cd client;
	npm run dev

ui-install:
	cd client;
	npm install;

ui-build:
	cd client;
	npm run build;


build: ui-build server-build

install-app:	server-install	ui-install


