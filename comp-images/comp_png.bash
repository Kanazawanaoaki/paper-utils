#!/bin/sh

# for file in `\find . -name '*.png'`; do
#     pngquant $file -o ${file}_test
#     mv ${file}_test $file
# done

for file in `\find . -name '*.png'`; do
    pngquant $file
done
