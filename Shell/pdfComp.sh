#!/bin/bash

# Compress a pdf file with GhostScript
# How to use : ./sPdfComp.sh exampleFile.pdf

if [ -z $1 ]; then
	echo '-> Error : no input file'
elif [ ! -e $1 ]; then
	echo '-> Error : file not found'
else
	echo '-> Compressing...'
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=out.pdf $1
	echo "-> Compressed file $1 done"
fi

