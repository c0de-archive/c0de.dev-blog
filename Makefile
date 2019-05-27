BASEDIR=$(CURDIR)
PLUGINDIR=$(BASEDIR)/plugins
PELICANDIR=$(BASEDIR)/pelican

help:
	@echo 'Makefile for installing and updating the c0de.dev blog                                    '
	@echo '                                                                                          '
	@echo 'Usage:                                                                                    '
	@echo '   make install                        Installs all components                            '
	@echo '   make uninstall                      Uninstalls all components, leaving the source dir  '
	@echo '   make update                         Replaces existing components that have changed     '
	@echo '   make plugins                        Creates symlinks of newly added plugins in pelican '
	@echo '                                                                                          '

install:
	@echo 'noop'

uninstall:
	@echo 'noop'

update:
	@echo 'noop'

plugins:
	@echo 'Creating symlinks for plugins'
	@echo 'noop'
