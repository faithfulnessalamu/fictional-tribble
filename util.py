def list_repos_from_file(filename):
    repo_list = []
    with open(filename) as fd:
        repo_list.extend(map(str.strip, fd.readlines()))
    return repo_list
