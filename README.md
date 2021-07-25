# fictional-tribble
Mass delete your GitHub repositories.

## WARNING
> **The delete action cannot be undone. It will permanently delete your specified repository, wiki, issues, comments, packages, secrets, workflow runs, and remove all collaborator associations.**

## Usage
To get started, you need to [create a new Github PAT](https://github.com/settings/tokens/new) with ```repo``` and ```delete_repo``` permissions:

The ```repo``` permission is required to list your private repositories.
![new_pat_repo_perm](https://raw.githubusercontent.com/thealamu/fictional-tribble/main/screenshots/pat1.png)

and the ```delete_repo``` permission is required to delete the repositories you choose.
![new_pat_del_repo_perm](https://raw.githubusercontent.com/thealamu/fictional-tribble/main/screenshots/pat2.png)

Copy the created PAT token and export as an environment variable:

```shell
export GITHUB_USERNAME=my_username
export GITHUB_PAT=my_pat_token
```

### CLI Usage
Get help
```bash
$ fictional-tribble --help
Usage: fictional-tribble [OPTIONS]

Options:
  -f, --file TEXT  File containing line-separated repository names
  -y               Skip delete verification
  --help           Show this message and exit.
```

Manually select the repositories you want to delete by running without any flags:
```shell
$ fictional-tribble
username/repo-test: Toy repo, felt cute, might delete later
Delete? (y/N): y

username/repo-of-code: Code solutions
Delete? (y/N): no

(forked) username/repo1: A Quiz/Game app
Delete? (y/N): n

(forked) username/repo-one: A one-off script
Delete? (y/N): yes

(forked) username/awesome-repo: List of awesome repos!
Delete? (y/N): no

Please verify you want to delete these repositories:
   repo-test repo-one [y/N]: y

Deleting repo-test...
Deleting repo-one...
```

You can also specify a file containing names of repositories to be deleted. Here's an example:
```shell
$ cat todelete.txt
repo-test
repo-one
```
```shell
$ fictional-tribble -f todelete.txt
Please verify you want to delete these repositories:
   repo-test repo-one [y/N]: y

Deleting repo-test...
Deleting repo-one...
```