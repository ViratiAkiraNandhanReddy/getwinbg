# getwinbg

`getwinbg` is a typed Python package and command-line utility for retrieving
the current Windows desktop background path.

```{toctree}
:maxdepth: 2
:caption: Contents

getting-started
api
cli
```

## At a glance

The package provides:

* A Python API through the {py:class}`getwinbg.Background` class.
* A CLI to display, reveal, open, or copy the current background path, and a
  Python API to access the path and perform file operations.
* Path validation so the returned value points to an existing file.

`getwinbg` supports Windows and requires Python 3.13 or newer.

## Quick start

Install the package from PyPI:

```console
$ pip install getwinbg
```

Read the current background path with Python:

```python
from getwinbg import Background

background = Background()
print(background.path)
```

Or use the command line:

```console
$ getwinbg background
```

See [Getting started](getting-started) for installation details and the
[Python API](api) and [CLI reference](cli) for the complete interfaces.

```{seealso}
* `getwinbg` on [PyPI](https://pypi.org/project/getwinbg/)
* [Source code on GitHub](https://github.com/ViratiAkiraNandhanReddy/getwinbg)
* [Changelog](https://github.com/ViratiAkiraNandhanReddy/getwinbg/blob/main/CHANGELOG.md)
```
