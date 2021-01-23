#!/bin/sh

for file in `\find . -name '*.jpg'`; do
    echo "$file"
    python crop_img_prosilica.py ${file#*/} crop-${file#*/}
done

for file in `\find . -name '*.png'`; do
    echo "$file"
    python crop_img_prosilica.py ${file#*/} crop-${file#*/}
done

