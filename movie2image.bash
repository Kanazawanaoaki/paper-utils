#!/bin/sh

movie2image () {
    file=$1
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
    # ffmpeg -i ${file} -ss 0 -t 10 -r 10 -f image2 ${name}/${name}-%06d.jpg
    ffmpeg -i ${file} -r 1 -f image2 -vcodec mjpeg -qscale 1 -qmin 1 -qmax 1 ${name}/${name}-%05d.jpg
}

for file in `\find . -name '*.mp4'`; do
    movie2image ${file}
done

for file in `\find . -name '*.MP4'`; do
    movie2image ${file}
done

for file in `\find . -name '*.MOV'`; do
    movie2image ${file}
done

for file in `\find . -name '*.avi'`; do
    movie2image ${file}
done
