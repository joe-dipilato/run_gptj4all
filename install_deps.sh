#!/usr/bin/env bash
curl -sSL https://install.python-poetry.org | python3 -
ln -s "$(brew --prefix)/bin/python"{3,} || true
poetry config virtualenvs.in-project true
poetry install