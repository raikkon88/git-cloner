import argparse, os
from lib.git import clone_to
import re

parser = argparse.ArgumentParser(
            prog = 'ProgramName',
            description = 'What the program does',
            epilog = 'Text at the bottom of help'
        )

parser.add_argument('--file', help='A file with all the repositories to clone')
parser.add_argument('--dest', help='The folder where to clone the repositories')

args = parser.parse_args()

if not os.path.exists(args.file):
    print('the file does not exists')
    quit()

with open(args.file, 'r') as reader: 
    repos = reader.readlines()

clonedRepos = 0
existingRepos = 0

for repo_url in repos: 
    if not os.path.exists(repo_url):
        clone_to(repo_url, args.dest)
        clonedRepos += 1
    else: 
        existingRepos += 1

print('{} repositories cloned, {} already exists.'.format(clonedRepos, existingRepos))