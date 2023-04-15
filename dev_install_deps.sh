#!/usr/bin/env sh

curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
curl -sSL https://install.python-poetry.org | python3 -
ln -s "$(brew --prefix)/bin/python"{3,}
poetry config virtualenvs.in-project true