import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('mp')         # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + foldername

g = Github("your git hub token")
user = g.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "#{repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master', ]

os.mkdir(_dir)

os.chdir(_dir)

# run one by one coomands
for c in commands:
    os.system(c)

print(f'{foldername} created locally')
# open vs code on created project folder in localmachine

with open('do_git.py', 'w') as fp:
    fp.write("""
import os
commit_message=str(input("Enter your commit message here : "))
commands = [
            'git init',
            'git add .',
            "git commit -m {}".format(commit_message),
            'git push -u origin master', ]
for c in commands:
    os.system(c)
""")
    fp.close()

with open('do_git.bat', 'w') as f:
    f.write("""
@echo off
python %~dp0\do_git.py %*
""")
    f.close()

with open('.gitignore', 'w') as fg:
    fg.write("""
do_git.py
do_git.bat
""")
    fg.close()
os.system('code .')
