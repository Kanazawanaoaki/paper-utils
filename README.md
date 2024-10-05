# paper-utils
論文を書く時に使うプログラムとか．


## 動画から画像を取り出す
```
ffmpeg -i 元動画.avi -ss 144 -t 148 -r 24 -f image2 %06d.jpg
```
-i 元動画.avi : 元動画  
-ss 144 : 抜き出し始点(秒)  
-t 148 : 抜き出し終点(秒)  
-r 24 : 1秒あたり何枚抜き出すか  
-f image2 %06d.jpg : jpeg で[000001.jpg]から連番で書き出し  
```
ffmpeg -i 元動画.avi -r 1 -f image2 -vcodec mjpeg -qscale 1 -qmin 1 -qmax 1 %05d.jpg
```
で高解像度に取り出すこともできる．とくに-rで一秒あたり何枚抜き出すかを変更する．  

それをディレクトリ内の全動画に実行するスクリプトもある．
```
bash movie2image.bash
```

## 動画から音声を抽出
```
ffmpeg -i input.mp4 output.mp3
```
それをディレクトリ内の全動画に実行するスクリプトもある．
```
bash audio_from_video.sh
```

## 画像のフォルダを動画にする
画像が入っているフォルダを指定して，指定したパスに動画を出力する．
```bash
python image_folder_to_video.py -i /home/kanazawa/Downloads/20240614_tracking_test/20240525_cup_test_images/rgb -o /home/kanazawa/Downloads/20240614_tracking_test/20240525_cup_test_images/20240525_cup_test_images.mp4
```

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

# フォルダ内のスクリプト

## crop-images
画像を切り出す．crop-imagesのフォルダを利用．

### 画像サイズ確認
```
python img_size.py [file_name]
```
で画像ファイルのサイズを見る．

### 画像をクロップ
crop_img_prosilica.pyを編集して範囲を指定する．少し分かりづらいかも．
```
python crop_img_prosilica.py [file_name] [cropped_file_name]
```
でクロップする．

### フォルダ内の画像をクロップ
フォルダ内の画像を同じ範囲で一気にクロップする．corp_img_prosilica.pyとcrop.bashがあるディレクトリに画像を全て入れて以下を実行．
```
bash crop.bash
```
でフォルダ内の.jpgと.pngのファイル(先頭にcropと付いていない画像ファイル全て)をcrop_img_prosilica.pyでクロップする．範囲を変えたい場合はcrop_img_prosilica.pyを変更．

## pdfmin
pdfの余白を取り除く

```
bash pdfmin.bash
```
でフォルダ内のpdfファイルの余白を取り除く．


## comp-images


## heic2jpg


## ros-topic-save