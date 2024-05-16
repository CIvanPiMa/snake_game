# The Snake Game

**NOTE**: if you come across this error:

```
  File ".../python3.12/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named '_tkinter'
```

[This post](https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos) has what you may need.


## Installation

```shell
pip install snake_game
```

## Usage

...TBD

## Contributing

Once you pull the repo, install the pre-commit hooks:

```shell
pre-commit install --install-hooks
```

Install the library (in a virtual environment) as an editable dependency with the development dependencies:

```shell
pip install -e ".[dev]"
```

And run the tests:

```shell
behave
```
