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
```
python crop_img_prosilica.py [file_name] [cropped file_name]
```
でクロップする．

### フォルダ内の画像をクロップ
```
bash crop.bash
```
でフォルダ内の.jpgと.pngのファイルをcrop_img_prosilica.pyでクロップする．

## pdfmin
pdfの余白を取り除く

```
bash pdfmin.bash
```
でフォルダ内のpdfファイルの余白を取り除く．

