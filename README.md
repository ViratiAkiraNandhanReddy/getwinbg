# getwinbg

Retrieve Windows background image paths from Python or the command line.

`getwinbg` is a lightweight Windows utility for accessing the current desktop background path.

## Features

* Retrieve the current Windows desktop background path
* Simple Python API
* Command-line interface
* Fully typed package (`py.typed`)

## Installation

### PyPI

```bash
pip install getwinbg
```

### From Source

```bash
git clone https://github.com/ViratiAkiraNandhanReddy/getwinbg.git
cd getwinbg

pip install .
```

## Usage

### CLI

```bash
getwinbg background
```

Example output:

```text
C:\Users\User\Pictures\wallpaper.jpg
```

### Python API

```python
from getwinbg import get_background

path = get_background()
print(path)
```

Example output:

```text
C:\Users\User\Pictures\wallpaper.jpg
```
