## crop-images
画像を切り出す．このディレクトリに画像を置いて利用．

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

