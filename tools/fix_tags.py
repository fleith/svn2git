#!/usr/local/bin/python3

import sys
import glob
import subprocess

path_to_search = sys.argv[1] if len(sys.argv) > 1 else "."

current = {}
current['user.name'] = subprocess.run("git config --get user.name", shell=True, check=True, stdout=subprocess.PIPE).stdout
current['user.email'] = subprocess.run("git config --get user.email", shell=True, check=True, stdout=subprocess.PIPE).stdout

print(current)

exit(0)

def svn_co_or_sw(filename):
    with open(filename, "r") as f:
        for line in f:
            try:
                subprocess.check_call('svn co {0}'.format(line), shell=True)
            except subprocess.CalledProcessError:
                subprocess.check_call('svn sw {0}'.format(line), shell=True)

for filename in glob.iglob('{0}/**/svnexternals.txt'.format(path_to_search), recursive=True):
    svn_co_or_sw(filename)

'''

  def fix_tags
      current = {}
      current['user.name']  = run_command("#{git_config_command} --get user.name", false)
      current['user.email'] = run_command("#{git_config_command} --get user.email", false)

      @tags.each do |tag|
        tag = tag.strip
        id      = tag.gsub(%r{^svn\/tags\/}, '').strip
        subject = run_command("git log -1 --pretty=format:'%s' \"#{escape_quotes(tag)}\"").chomp("'").reverse.chomp("'").reverse
        date    = run_command("git log -1 --pretty=format:'%ci' \"#{escape_quotes(tag)}\"").chomp("'").reverse.chomp("'").reverse
        author  = run_command("git log -1 --pretty=format:'%an' \"#{escape_quotes(tag)}\"").chomp("'").reverse.chomp("'").reverse
        email   = run_command("git log -1 --pretty=format:'%ae' \"#{escape_quotes(tag)}\"").chomp("'").reverse.chomp("'").reverse
        run_command("#{git_config_command} user.name \"#{escape_quotes(author)}\"")
        run_command("#{git_config_command} user.email \"#{escape_quotes(email)}\"")

        original_git_committer_date = ENV['GIT_COMMITTER_DATE']
        ENV['GIT_COMMITTER_DATE'] = escape_quotes(date)
        run_command("git tag -a -m \"#{escape_quotes(subject)}\" \"#{escape_quotes(id)}\" \"#{escape_quotes(tag)}\"")
        ENV['GIT_COMMITTER_DATE'] = original_git_committer_date

        run_command("git branch -d -r \"#{escape_quotes(tag)}\"")
      end

    ensure
      # We only change the git config values if there are @tags available.  So it stands to reason we should revert them only in that case.
      unless @tags.empty?
        current.each_pair do |name, value|
          # If a line was read, then there was a config value so restore it.
          # Otherwise unset the value because originally there was none.
          if value.strip != ''
            run_command("#{git_config_command} #{name} \"#{value.strip}\"")
          else
            run_command("#{git_config_command} --unset #{name}")
          end
        end
      end
    end
'''
