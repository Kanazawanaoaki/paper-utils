#!/bin/sh

for file in `\find . -name '*.jpg'`; do
    tmp=${file#*/}
    echo ${tmp%.*}
    convert ${file#*/} ${tmp%.*}.png
done
