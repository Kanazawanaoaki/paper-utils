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

## crop-images
画像を切り出す

### 画像サイズ確認
```
python img_size.py [file_name]
```
で画像ファイルのサイズを見る．

### 画像をクロップ
crop_img_prosilica.pyを編集して範囲を指定する．
```
python crop_img_prosilica.py [file_name] [cropped_file_name]
```
でクロップする．

### フォルダ内の画像をクロップ
フォルダ内の画像を同じ範囲で一気にクロップする．corp_img_prosilica.pyとcrop.bashがあるディレクトリに画像を入れて以下を実行．
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

