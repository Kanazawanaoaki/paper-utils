#!/bin/bash

# フォルダ内のすべてのMOVファイルに対して処理を行う
for input_mov_file in *.MOV; do
    if [ -f "$input_mov_file" ]; then
        output_audio_file="audio-${input_mov_file%.*}.mp3"
        ffmpeg -i "$input_mov_file" "$output_audio_file"
        echo "Extracted audio from $input_mov_file to $output_audio_file"
    fi
done

# フォルダ内のすべてのmp4ファイルに対して処理を行う
for input_mov_file in *.mp4; do
    if [ -f "$input_mov_file" ]; then
        output_audio_file="audio-${input_mov_file%.*}.mp3"
        ffmpeg -i "$input_mov_file" "$output_audio_file"
        echo "Extracted audio from $input_mov_file to $output_audio_file"
    fi
done
