#!/bin/sh

for file in `\find . -name '*.png'`; do
    tmp=${file#*/}
    echo ${tmp%.*}
    convert ${file#*/} -quality 85  ${tmp%.*}.jpg
done
