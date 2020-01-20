#!/bin/bash

# Cut a specific number of lines at the beginning of a file
# Replace comma by space

read -p 'Number of lines to cut: ' lc
let lc--
		
for file in "$@"
do
	if [ ! -e $file ]; then
		echo '-> Error: file not found'
	else
		fileCut=$( echo $file | cut -d. -f 1 )
		echo "Processing $fileCut ..."
		sed "1,${lc}d" $file > "${fileCut}_cut.txt"
		sed -i 's/,/\ /g' "${fileCut}_cut.txt"
	fi
done