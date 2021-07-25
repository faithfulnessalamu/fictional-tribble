def list_repos_from_file(filename):
    repo_list = []
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            if line:
                repo_list.append(line)

    return repo_list
