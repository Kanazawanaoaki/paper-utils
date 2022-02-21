#!/bin/sh

for file in `\find . -name '*-bags'`; do
    after_sra=${file#*/}
    name=${after_sra%%.*}
	echo "$name"
    mkdir_one_line=movies/${name}
    if [[ -d "$mkdir_one_line" ]]; then
        echo "既に"$mkdir_one_line"は存在しています"
    else
        mkdir "$mkdir_one_line"
        echo ""$mkdir_one_line"を作りました"
    fi    
    python comp_rosbag_to_movie.py -b ${name} -d movies/${name}
done
