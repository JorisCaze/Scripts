#!/bin/bash

# Compress a pdf file with GhostScript

if [-n $#]; then
	echo '-> Compressing...'
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=out.pdf $1
	echo "-> Compressed file $1 done"
else
	echo '-> Error : no input file'
fi

