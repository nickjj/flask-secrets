.DEFAULT_GOAL := help

.PHONY: help
help:
				@printf "%s\n" "Available targets:"
				@printf "%s\n" "  make install"
				@printf "%s\n" "  make uninstall"
				@printf "%s\n" "  make clean"
				@printf "%s\n" "  make build"
				@printf "%s\n" "  make publish"

.PHONY: install
install:
				@printf "%s\n" "Installing package to dev environment..."
				pip3 install --user --editable .

.PHONY: uninstall
uninstall:
				@printf "%s\n" "Uninstalling package from dev environment..."
				python3 setup.py develop --user -u

.PHONY: clean
clean:
				@printf "%s\n" "Cleaning package..."
				python3 setup.py sdist clean --all
				rm -rf build/ dist/ *.egg-info/

.PHONY: build
build:
				@printf "%s\n" "Building package..."
				python3 setup.py sdist bdist_wheel

.PHONY: publish
publish:
				@printf "%s\n" "Publishing package to PyPi..."
				python3 setup.py sdist upload
