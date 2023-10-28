# Makefile for Python project.

PYTHON3 ?= python3

MODULE = pyrube

all:

.PHONY:
check: lint mypy pycodestyle

.PHONY:
pylint:
	@pylint $(MODULE)

.PHONY:
mypy:
	@mypy --strict $(MODULE)

.PHONY:
pycodestyle:
	@$(PYTHON3) -m pycodestyle $(MODULE)

# vim: set ts=8 noet sts=8:
