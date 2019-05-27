SHELL := /bin/bash

help:
	@echo 'Makefile for installing and updating the c0de.dev blog                                    '
	@echo '                                                                                          '
	@echo 'Usage:                                                                                    '
	@echo '   make install                        Installs all components                            '
	@echo '   make uninstall                      Uninstalls all components, leaving the source dir  '
	@echo '   make update                         Replaces existing components that have changed     '
	@echo '                                                                                          '

install:
	@echo 'Installing pelican dependancies'
	@virtualenv venv
	@source venv/bin/activate
	@pip install -r requirements.txt

uninstall:
	@echo 'noop'

update:
	@echo 'Updating your pelican install'
	@git submodule update --recursive --remote
	@source venv/bin/activate
	@pip install -r requirements.txt
