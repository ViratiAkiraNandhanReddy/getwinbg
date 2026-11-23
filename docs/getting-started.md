# Getting started

## Requirements

* Windows
* Python 3.13 or newer

The package reads the background configured for the current Windows user. It
does not download or change wallpapers.

## Installation

Install the latest published release:

```console
$ python -m pip install getwinbg
```

Install from a source checkout:

```console
$ git clone https://github.com/ViratiAkiraNandhanReddy/getwinbg.git
$ cd getwinbg
$ python -m pip install .
```

## First use

The Python API returns a string containing the path to the current background:

```python
from getwinbg import Background

background = Background()
print(background.path)
```

The equivalent CLI command displays the path in a formatted panel:

```console
$ getwinbg background
```

If Windows does not have a usable background file configured, the package
raises an error rather than returning an invalid path. The CLI displays the
error and exits with a non-zero status.

## Development installation

Install the optional development tools from the repository root:

```console
$ python -m pip install -e ".[dev]"
```

Run the project checks:

```console
$ ruff check .
$ ruff format --check .
$ ty check
```

Build the documentation locally:

```console
$ python -m pip install -r docs/requirements.txt
$ python -m sphinx -W --keep-going docs docs/_build/html
```
