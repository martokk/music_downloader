import typer
from loguru import logger
from rich.console import Console

from music_downloader import version
from music_downloader.downloader import Downloader

# Configure Loguru Logger
logger.add("log.log", level="TRACE", rotation="50 MB")

# Configure Rich Console
console = Console()

# Configure Typer
app = typer.Typer(
    name="music_downloader",
    help="A wrapper for common music downloaders.",
    add_completion=False,
)


# Print Current Version
def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]music_downloader[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


# Typer Commands
@app.command()
def main(
    service: str = typer.Argument(..., help="Downloader Service to use"),
    url: str = typer.Argument(..., help="URL"),
    save_to: str = typer.Argument(..., help="Save To Directory"),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the music_downloader package.",
    ),
) -> None:

    # Example Entry Point
    console.print(f"CLI: {service=} {url=} {save_to=}")
    logger.info(f"CLI: {service=} {url=} {save_to=}")

    Downloader(service_str=service, url=url, save_to=save_to).download()


if __name__ == "__main__":
    app()
