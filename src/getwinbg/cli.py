import typer
from getwinbg.api import get_background

app = typer.Typer(
    name="getwinbg",
    help="Retrieve Windows background images.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """getwinbg CLI."""
    pass


@app.command()
def background() -> None:
    """Retrieve the current desktop background."""

    typer.echo(get_background())
