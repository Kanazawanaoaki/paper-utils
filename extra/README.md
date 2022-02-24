# paper-utils extra

## グレイスケールに変換する

```
python grey_scale_conv.py [file_name] [grey_file_name]
```

### フォルダ内の画像をグレイスケール変換

```
bash grey.bash
```

## pngとjpgの変換

pngからjpgに変換
```
convert image.png -quality 85 image.jpg
```

フォルダ内の画像をpngからjpgに変換する
```
bash png2jpg-convert.bash
```

jpgからpngに変換
```
convert image.jpg image.png
```

フォルダ内の画像をjpgからpngに変換する
```
bash jpg2png-convert.bash
```

