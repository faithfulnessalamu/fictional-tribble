import click

from api import github
from os import getenv
from os.path import isfile
from util import list_repos_from_file
from functools import partial

API_TOKEN_KEY = "GITHUB_PAT"


@click.command()
@click.option(
    "-f",
    "--file",
    "filename",
    help="File containing line-separated repository names",
)
@click.option(
    "-y", "skip_verify", is_flag=True, default=False, help="Skip delete verification"
)
def cli(filename, skip_verify):
    github_api = github.Api(getenv(API_TOKEN_KEY))

    # define where the repo list should come from,
    # file takes precedence over API
    repo_list_source = None
    if filename:
        if isfile(filename):
            repo_list_source = partial(list_repos_from_file, filename)
        else:
            raise Exception(f"'{filename}': No such file")
    else:
        repo_list_source = github_api.list_user_repos

    # obtain the repositories to be deleted, potentially an API call
    repositories = repo_list_source()

    if not skip_verify:
        # filter out whichever repo the user declines
        print("Please verify you want to delete these repositories:")
        if not is_verified(repositories):
            print("No changes effected, your repositories are intact")
            return


def is_verified(repositories):
    return input(f"{' '.join(repositories)} (y/N): ").lower() in ['y', 'yes']


if __name__ == "__main__":
    cli()
