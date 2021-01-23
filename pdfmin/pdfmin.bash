#!/bin/sh

function pdfmin() {
    pdfcrop $1
    mv "${1:0:-4}-crop.pdf" $1
} 

command="pdfmin $file"
for file in `\find . -name '*.pdf'`; do
    # eval $command
    pdfmin $file
done
