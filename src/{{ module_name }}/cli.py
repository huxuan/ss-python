"""Command Line Interface."""
import typer

app = typer.Typer()


@app.callback()
def callback() -> None:
    """CLI for Serious Scaffold Python."""


@app.command()
def run() -> None:
    """Run command."""


typer_click_object = typer.main.get_command(app)


if __name__ == "__main__":
    app()  # pragma: no cover
