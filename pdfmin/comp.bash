#!/bin/sh

command="pdfmin $file"
for file in `\find . -name '*.pdf'`; do
    if [ ${file%%_*} = ./compressed ]; then
	echo "$file"
    else
        echo ${file#*/}
        gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed_${file#*/} ${file#*/}
    fi
done
