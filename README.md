# First steps

- Create a new repository on GitHub with the name `snake_game`.

- Then run the following commands to initialize the repository:

```shell
git init --initial-branch=main
git add README.md
git commit -m "Initial commit"
git remote add origin git@github.com:CIvanPiMa/snake_game.git
git push -u origin main
```

- Finally, checkout to a development branch and push the initial project structure:

```shell
BRANCH_NAME=feat/initial_project_release
git checkout -b ${BRANCH_NAME}
git add .
git commit -m "feat: Add initial project structure"
git push --set-upstream origin ${BRANCH_NAME}
```

---

# The Snake Game

TBD

## Installation

```shell
pip install The Snake Game
```

## Usage

...TBD

## Contributing

Once you pull the repo, install the pre-commit hooks:

```shell
pre-commit install --install-hooks
```

Install the library as editable with the development dependencies:

```shell
pip install -e ".[dev]"
```

And run the tests:
```shell
behave
```