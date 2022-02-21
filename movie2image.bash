#!/bin/sh

for file in `\find . -name '*.mp4'`; do
    after_sra=${file#*/}
    name=${after_sra%%.*}
	echo "$name"
    mkdir_one_line=${name}
    if [[ -d "$mkdir_one_line" ]]; then
        echo "既に"$mkdir_one_line"は存在しています"
    else
        mkdir "$mkdir_one_line"
        echo ""$mkdir_one_line"を作りました"
    fi    
    ffmpeg -i ${name}.mp4 -ss 0 -t 10 -r 10 -f image2 ${name}/${name}-%06d.jpg
done
