# getwinbg

Retrieve the current Windows desktop background from Python or the command
line.

`getwinbg` is a lightweight, typed Windows utility that returns the path to
the current desktop background and can optionally reveal or open it, or copy
its path to the clipboard.

[Read the full documentation](https://getwinbg.readthedocs.io/).

## Features

* Retrieve the current Windows desktop background path
* Reveal the background in File Explorer
* Open the background with its default application
* Copy the background path to the Windows clipboard
* Python API and command-line interface
* Fully typed package (`py.typed`)

## Requirements

* Windows
* Python 3.13 or newer

## Installation

Install the latest release from PyPI:

```bash
pip install getwinbg
```

To install the current source checkout:

```bash
git clone https://github.com/ViratiAkiraNandhanReddy/getwinbg.git
cd getwinbg
pip install .
```

## Usage

### CLI

Display the current desktop background:

```bash
getwinbg background
```

Reveal the background file in File Explorer:

```bash
getwinbg background --reveal
```

Open the file with its default image application:

```bash
getwinbg background --open
```

Copy the path as text to the Windows clipboard:

```bash
getwinbg background --copy
```

Use `-r`, `-o`, and `-c` as short forms for `--reveal`, `--open`, and
`--copy`. These options can be combined. Copying places the path on the
clipboard; it does not copy the image file. The global `--version` option
prints the installed package version:

```bash
getwinbg --version
```

Example output from `getwinbg background`:

```text
                     $$\                   $$\           $$\                 
                     $$ |                  \__|          $$ |                
 $$$$$$\   $$$$$$\ $$$$$$\   $$\  $$\  $$\ $$\ $$$$$$$\  $$$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\\_$$  _|  $$ | $$ | $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$$$$$$$ | $$ |    $$ | $$ | $$ |$$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |
$$ |  $$ |$$   ____| $$ |$$\ $$ | $$ | $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$$ |\$$$$$$$\  \$$$$  |\$$$$$\$$$$  |$$ |$$ |  $$ |$$$$$$$  |\$$$$$$$ |
 \____$$ | \_______|  \____/  \_____\____/ \__|\__|  \__|\_______/  \____$$ |
$$\   $$ |                                                         $$\   $$ |
\$$$$$$  |                                                         \$$$$$$  |
 \______/                                                           \______/ 

             Retrieve Windows background image paths  •  vX.X.X

╭───────────────────────────────── getwinbg ─────────────────────────────────╮
│ Current desktop background                                                 │
│                                                                            │
│ C:\Users\User\Pictures\wallpaper.jpg                                       │
╰────────────────────────────────────────────────────────────────────────────╯
```

### Python API

The recommended API is the `Background` class:

```python
from getwinbg import Background

background = Background()
print(background.path)

background.reveal()
background.open()
background.copy()
```

Example output:

```text
C:\Users\User\Pictures\wallpaper.jpg
```

`get_background()` remains available for compatibility but is deprecated and
will be removed in version 0.2.0. Use `Background().path` instead:

```python
from getwinbg import get_background

path = get_background()
```

## Development

Install the development dependencies and run the checks:

```bash
pip install -e ".[dev]"
ruff check .
ruff format --check .
ty check
```

Build the documentation locally:

```bash
pip install -r docs/requirements.txt
python -m sphinx -W --keep-going docs docs/_build/html
```

## License

`getwinbg` is released under the [MIT License](LICENSE).
