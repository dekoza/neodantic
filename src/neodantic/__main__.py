"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Neodantic."""


if __name__ == "__main__":
    main(prog_name="neodantic")  # pragma: no cover
