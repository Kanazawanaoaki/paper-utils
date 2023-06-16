#!/bin/sh

for file in `\find . -name '*.jpg'`; do
    if [ ${file%%-*} = ./crop ]; then
	echo "$file"
    else
	python crop_img_prosilica.py -o ${file#*/} -c crop-${file#*/}
    fi
done

for file in `\find . -name '*.png'`; do
    if [ ${file%%-*} = ./crop ]; then
	echo "$file"
    else
	python crop_img_prosilica.py -o ${file#*/} -c crop-${file#*/}
    fi
done
