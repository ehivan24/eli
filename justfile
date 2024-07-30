set export

COMMIT := `git rev-parse --short HEAD`
REPO_URL := `(git config --get remote.origin.url)`
_VERSION := "2024.7.1"  # EDITED BY BUMPVER, NO TOUCH

@install:
    poetry build
    poetry install

@build:
    just release-info
    just make-pretty
    just install

[private]
@make-pretty:
    poetry run black eli/
    poetry run isort eli/
    poetry run ruff check --fix eli/

[private]
@release-info:
    figlet "$_VERSION" | lolcat
    cowsay "${REPO_URL} ${COMMIT} ${_VERSION}" | lolcat


@prepare-version:
    poetry run bumpver update
    poetry run bumpver show --no-fetch

