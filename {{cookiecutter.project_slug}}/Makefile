.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"



# ----------------------------------------------------------
# Helpers
# ----------------------------------------------------------
.PHONY: help

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


# ----------------------------------------------------------
# Coding Helpers
# ----------------------------------------------------------

clean: clean-build clean-pyc clean-test docker-clean ## remove all build, test, coverage and Python artifacts




# ----------------------------------------------------------
# docker Setup
# ----------------------------------------------------------
.PHONY: docker-build docker-clean docker-run docker-test

docker-build: ## build and execute server in a docker container
	sudo docker compose build

docker-run: docker-build ## build and execute server in a docker container
	sudo docker compose up --build

docker-test: docker-build ## test server in a docker container
	sudo docker compose run --rm web-server python -m pytest

docker-clean: ## clean container
	sudo docker rm web-server


# ----------------------------------------------------------
# Test Helpers
# ----------------------------------------------------------
.PHONY: test test-parallel test-all clean-test ptw

test: ## run tests quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	pytest
{%- else %}
	python setup.py test
{%- endif %}

test-parallel: ## run parallel pytests with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	pytest -n 5
{%- else %}
    echo "not implemented"
{%- endif %}

test-all: ## run tests on every Python version with tox
	tox

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

ptw: ## pytest-watch
	ptw -- -s -n 2


# ----------------------------------------------------------
# Code Quality Helpers
# ----------------------------------------------------------
.PHONY: coverage lint lint/flake8
{%- if cookiecutter.use_black == 'y' %} lint/black{% endif %}

coverage: ## check code coverage quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	coverage run --source {{ cookiecutter.project_slug }} -m pytest	
    coverage run -a --source tests -m pytest
{%- else %}
	coverage run --source {{ cookiecutter.project_slug }} setup.py test
{%- endif %}

	# coverage combine
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

lint/flake8: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

{%- if cookiecutter.use_black == 'y' %}
lint/black: ## check style with black
	black --check {{ cookiecutter.project_slug }} tests
{%- endif %}

lint: lint/flake8{%- if cookiecutter.use_black == 'y' %} lint/black{%- endif %} ## check style

# ----------------------------------------------------------
# Documentation Helpers
# ----------------------------------------------------------
.PHONY: docs livehtml #servedocs

# ----------------------------------------------------------
# Sphinx Parameters
# ----------------------------------------------------------
# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = python-coding-challenge
SOURCEDIR     = docs
BUILDDIR      = docs/_build
AUTODIR       = docs/_autosummary
PORT          = 8086
IGNORE        = "*.log"

# seconds before opening the browser
AUTODELAY     = 0

# a sleep to avoid too much CPU use while typing documentation
# and the system is rebuilind too fast
AUTOOPS       = --pre-build "sleep 1"

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

#servedocs: docs ## compile the docs watching for changes
#	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

livehtml:
	nice sphinx-autobuild -b html $(ALLSPHINXOPTS) --open-browser --port $(PORT) --watch .. --re-ignore "\.git/" $(SOURCEDIR) $(BUILDDIR)/html --ignore $(IGNORE) --delay $(AUTODELAY) $(AUTOOPS)

clean-doc: ## remove docs artifacts
	rm -fr docs/_build

# ----------------------------------------------------------
# Environment Setup
# ----------------------------------------------------------
.PHONY: install-testing-requisites

install-testing-requisites: ## install testing requisites
	@pip install -r requirements/base.txt
	@pip install -r requirements/testing.txt

# ----------------------------------------------------------
# Deployment Helpers
# ----------------------------------------------------------
.PHONY: release dist install clean-build clean-pyc

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

