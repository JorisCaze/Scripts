#!/bin/bash

# Extract public repository names of a GitHub user
# How to use : ./extractGHrepos.sh USER

if [ -z $1 ]; then 
	echo '-> Error : no input user'
else
	echo "-> Looking for $1 repos on GitHub..."
 	curl -s "https://api.github.com/users/$1/repos?per_page=100" | grep -o 'git@[^"]*' | cut -d/ -f 2 | cut -d. -f 1
fi

# MEMO cut
# -d/ :: cut at the character /
# -f :: 1 keep left part - 2 keep right part  