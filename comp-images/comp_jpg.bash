#!/bin/sh

quo=50
for file in `\find . -name '*.jpg'`; do
    jpegoptim $file -m $quo
done
