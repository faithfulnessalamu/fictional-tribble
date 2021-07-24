import click


@click.command()
@click.option(
    "-f",
    "--file",
    "filename",
    default=None,
    help="File containing line-separated repository names",
)
@click.option(
    "-y", "skip_verify", is_flag=True, default=False, help="Skip delete verification"
)
def cli(filename, skip_verify):
    pass


if __name__ == "__main__":
    cli()
