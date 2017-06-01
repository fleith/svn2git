# svn2git
Create a git repository from a svn repo (Python wrapper over git-svn)

## TODO
 - accept branchs inside branchs
 - guess branchs by pattern file name
 - ...

### steps

Init git svn:

	git svn init --prefix=svn/ --no-metadata --tags tags/1.0/ --tags tags/1.2 --trunk trunk --branches 1.2 --branches 2.0  svn://uri
 
	git config svn.authorsfile /home/alvaro/.svn2git/authors
 
Fetch:

	git svn fetch
 
Fix branches:

    git branch -r --no-color | grep -v \/tags\/ | grep -v 'svn\/trunk' | cut -c 7- | while read line ; do git checkout -b $line remotes/svn/$line ; done
    
Fix tags:

    fix_tags.py
    
Fix trunk:

    git checkout svn/trunk
    git branch -D master
    git checkout -f -b master
    
Optimize repos:

    git gc
