#!/bin/bash

# Compress a pdf file with GhostScript

read -p '-> Enter file name to compress : ' file
echo '-> Compressing...'

gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=out.pdf $file

echo "-> Compressed file $file done"
