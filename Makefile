.PHONY: all upgrade-pip install-deps

all: upgrade-pip install-deps

upgrade-pip:
	pip install --upgrade pip

install-deps:
	pip install --requirement requirements.txt
