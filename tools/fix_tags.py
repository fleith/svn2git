#!/usr/local/bin/python3
import os
import sys
import subprocess

path_to_search = sys.argv[1] if len(sys.argv) > 1 else "."
print("stdout encoding: ", sys.stdout.encoding)


def git_command_stdout(command):
    return subprocess.run("git {0}".format(command), shell=True, check=True,
                          stdout=subprocess.PIPE).stdout.decode(sys.stdout.encoding).rstrip()


current_user_name = git_command_stdout('config --get user.name')
current_user_email = git_command_stdout('config --get user.email')
current_committer_date = os.environ['GIT_COMMITTER_DATE'] if 'GIT_COMMITTER_DATE' in os.environ else None

print('current user.name: ', current_user_name)
print('current user.email: ', current_user_email)
print("current committer date: ", current_committer_date)

# TODO: load tags from args or file
tags = ['svn/tags/tag-a', 'svn/tags/tag-b']

for tag in tags:
    tag_id = tag.split('svn/tags/', 1)[1].strip()
    # git show head~0 --no-patch --pretty=format:'%ae'
    subject = git_command_stdout("log -1 --pretty=format:'%s' \"{0}\"".format(tag))
    date = git_command_stdout("log -1 --pretty=format:'%ci' \"{0}\"".format(tag))
    author = git_command_stdout("log -1 --pretty=format:'%an' \"{0}\"".format(tag))
    email = git_command_stdout("log -1 --pretty=format:'%ae' \"{0}\"".format(tag))
    print(tag_id, subject, date, author, email)
    git_command_stdout('config user.name \"{0}\"'.format(author))
    git_command_stdout('config user.email \"{0}\"'.format(email))
    os.environ['GIT_COMMITTER_DATE'] = date
    print('creating tag name:{0} origin:{1}'.format(tag_id, tag))
    git_command_stdout("tag -a -m \"{0}\" \"{1}\" \"{2}\"".format(subject, tag_id, tag))
    print('deleting branch name:{0}'.format(tag))
    git_command_stdout("branch -d -r \"{0}\"".format(tag))

if current_committer_date is None:
    os.environ.pop('GIT_COMMITTER_DATE', None)
else:
    os.environ['GIT_COMMITTER_DATE'] = current_committer_date

if current_user_name:
    git_command_stdout('config user.name \"{0}\"'.format(current_user_name))
if current_user_email:
    git_command_stdout('config user.email \"{0}\"'.format(current_user_email))
