# panel-rec-set
パネル認識のためのセット

## パネル認識システムの作り方
実際に認識したいもののrosbagをとっておく．rosbagのとり方はhogehoge.TODO  

### rosbagから画像データをとる
まずはrosbagを流す
```
roslaunch jsk_2020_04_pr2_curry rosbag_play_curry_test.launch rosbag:=/mnt/hdd0/rosbags/PR2/20211016_kanazawa_kitchen/20211016_kitchen_02.bag gui:=true
```
```
rosrun image_view image_view image:=/prosilica/image_raw
```

```
roslaunch jsk_2020_04_pr2_curry data_collection_prosilica.launch
```

```
rosservice call /after_stow_data_collection/save_request "{}"
```

### 画像データを加工する
HP(z800)の/mnt/hdd0/rosbags/data_collection/ih-panel-recにフォルダがある．  
そこのプログラムとかを使ってやる感じ．  
現状は`crop_img_prosilica.py`を調整してから，
```
bash crop.bash
```
を実行して．画像をクロップして．`/png-cropped-img`内に移動して
```
bash grey.bash
```
を実行して，画像をグレイスケールにして，
```
bash png2jpg-convert.bash
```
を実行して，jpgに変換する．

### 認識のlaunchファイルを作る
作るプログラムとしては，
このcommit(https://github.com/Kanazawanaoaki/jsk_demos/commit/0f89c7a5023230260f0a980b48fa7104276b5425 )のように追加をすればよくて，

dataフォルダ : https://github.com/Kanazawanaoaki/jsk_demos/tree/kanazawa-ow/jsk_2020_04_pr2_curry/data/ih-panel-stove-20211016  
center_1016_ih_panel_reader.launch : https://github.com/Kanazawanaoaki/jsk_demos/blob/kanazawa-ow/jsk_2020_04_pr2_curry/launch/sift/center_1016_ih_panel_reader.launch  
update_1016_ih_panel_stove_reader.launch : https://github.com/Kanazawanaoaki/jsk_demos/blob/kanazawa-ow/jsk_2020_04_pr2_curry/launch/sift/update_1016_ih_panel_stove_reader.launch  
template-1016-ih-stove.yaml : https://github.com/Kanazawanaoaki/jsk_demos/blob/kanazawa-ow/jsk_2020_04_pr2_curry/launch/sift/template-1016-ih-stove.yaml 

