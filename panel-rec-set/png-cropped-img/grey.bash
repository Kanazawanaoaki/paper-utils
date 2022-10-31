#!/bin/sh

for file in `\find . -name '*.jpg'`; do
    if [ ${file%%-*} = ./grey ]; then
	echo "$file"
    else
	python grey_scale_conv.py ${file#*/} grey-${file#*/}
    fi
done

for file in `\find . -name '*.png'`; do
    if [ ${file%%-*} = ./grey ]; then
	echo "$file"
    else
	python grey_scale_conv.py ${file#*/} grey-${file#*/}
    fi
done
