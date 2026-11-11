from pathlib import Path

import typer
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from getwinbg.__version__ import __version__
from getwinbg.api import get_background

console = Console()

app = typer.Typer(
    name="getwinbg",
    help=(
        "Your all-in-one toolkit for exploring Windows wallpapers — "
        "from current desktop backgrounds and built-in presets to "
        "cached Bing images and Spotlight collections."
    ),
    no_args_is_help=True,
)

_BANNER = r"""
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
"""


@app.callback()
def main() -> None:
    """getwinbg CLI."""
    console.print(
        Align.center(Text(_BANNER.strip("\n"), style="bold cyan")),
    )
    console.print(
        Align.center(
            Text.from_markup(
                "Your toolkit for exploring Windows wallpapers  •  "
                "[link=https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/"
                f"tag/v{__version__}]v{__version__}[/link]",
                style="dim",
            )
        ),
    )
    console.print()


@app.command()
def background() -> None:
    """Retrieve the current desktop background."""

    try:
        path = get_background()
    except Exception as error:
        console.print(
            Panel(
                f"[bold red]Could not retrieve the desktop background.[/bold red]\n"
                f"[dim]{error}[/dim]",
                title="getwinbg",
                border_style="red",
            )
        )
        raise typer.Exit(code=1) from error

    console.print(
        Panel(
            f"[bold green]Current desktop background[/bold green]\n\n"
            f"[link={Path(path).resolve().as_uri()}]{path}[/link]",
            title="getwinbg",
            border_style="cyan",
        )
    )
