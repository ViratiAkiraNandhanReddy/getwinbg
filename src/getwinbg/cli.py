from pathlib import Path
from typing import Annotated

import typer
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from getwinbg.__version__ import __version__
from getwinbg.api import Background

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

_TITLE = "getwinbg"
_BORDER_STYLE = "cyan"
_ERROR_BORDER_STYLE = "red"


class CommandCLI:
    """Shared presentation helpers for individual CLI command handlers."""

    def __init__(self, console: Console) -> None:
        self.console = console

    def show_error(self, message: str, error: Exception) -> None:
        """Display a consistent error message in the CLI."""
        self.console.print(
            Panel(
                f"[bold red]{message}[/bold red]\n[dim]{error}[/dim]",
                title=_TITLE,
                border_style=_ERROR_BORDER_STYLE,
            )
        )


class ApplicationCLI(CommandCLI):
    """Presentation layer for application-wide CLI output."""

    def show_banner(self) -> None:
        """Display the application banner and version."""
        self.console.print()
        self.console.print(
            Align.center(
                Text(
                    _BANNER.strip("\n"),
                    style="bold cyan",
                )
            )
        )
        self.console.print(
            Align.center(
                Text.from_markup(
                    "Your toolkit for exploring Windows wallpapers  •  "
                    "[link=https://github.com/ViratiAkiraNandhanReddy/getwinbg/releases/"
                    f"tag/v{__version__}]v{__version__}[/link]",
                    style="dim",
                )
            )
        )
        self.console.print()


class BackgroundCLI(CommandCLI):
    """Presentation and interaction layer for the ``background`` command."""

    def display(self, path: Path) -> None:
        """Display the path of the current desktop background."""
        self.console.print(
            Panel(
                "[bold green]Current desktop background[/bold green]\n\n"
                f"[link={path.as_uri()}]{path}[/link]",
                title=_TITLE,
                border_style=_BORDER_STYLE,
            )
        )

    def reveal(self, background: Background) -> None:
        """Ask File Explorer to reveal the background file."""
        try:
            background.reveal()
        except Exception as error:
            self.show_error("Could not reveal the desktop background.", error)
            raise typer.Exit(code=1) from error

        self.console.print(
            "[dim]Requested File Explorer to reveal the desktop background.[/dim]"
        )


application_cli = ApplicationCLI(console)
background_cli = BackgroundCLI(console)

VersionOption = Annotated[
    bool,
    typer.Option(
        "--version",
        help="Display the current version of getwinbg.",
    ),
]


@app.callback(invoke_without_command=True)
def main(version: VersionOption = False) -> None:
    """getwinbg CLI."""
    if version:
        console.print(Text(f"getwinbg {__version__}"))
        raise typer.Exit()

    application_cli.show_banner()


RevealOption = Annotated[
    bool,
    typer.Option(
        "--reveal",
        "-r",
        help="Reveal the current desktop background.",
    ),
]


@app.command()
def background(
    _reveal: RevealOption = False,
) -> None:
    """Retrieve the current desktop background."""

    try:
        background = Background()
        path = Path(background.path).resolve()
    except Exception as error:
        background_cli.show_error("Could not retrieve the desktop background.", error)
        raise typer.Exit(code=1) from error

    background_cli.display(path)

    if _reveal:
        background_cli.reveal(background)
