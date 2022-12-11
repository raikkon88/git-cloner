import os, re

def clone(repository):
    command = 'git clone {}'.format(repository)
    os.system(command)

def clone_to(repository, destiny):
    folder_name = extract_folder_name(repository)
    clone(repository=repository)
    command = "mv {} {}".format(folder_name, destiny)
    os.system(command)

def match_repository_path(repository_url):
    match = re.search('git@github.com:(.*)\/(.*)\.git', repository_url)
    return match.group(1), match.group(2)

def extract_folder_name(repository_url): 
    _, repo = match_repository_path(repository_url)
    return repo