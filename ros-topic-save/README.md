# ROS topic save
ROSトピックの保存方法についてメモなど．

## data collection server
data collection serverを使う．サンプルのlaunchがある．

## image topic save
[iamge_saver](http://wiki.ros.org/image_view#image_view.2Fdiamondback.image_saver )
```
rosrun image_view image_saver image:=/camera/rgb/image_raw _filename_format:=left%04d.%s
```
save with service
```
rosrun image_view image_saver image:=/camera/rgb/image_raw _save_all_image:=false _filename_format:=left%04d.%s
```
```
rosservice call /image_saver_[hogehoge]/save
```

## image topic to movie
```
rosrun image_view video_recorder image:=/camera/rgb/image_raw _filename:=vegs-into-pot-2020-05-20-17-52-10.avi
```

## comp image topic to movie
```
cd scripts
python comp_rosbag_to_movie.py -b bags/ -d movies/
```
or
```
bash comp_rosbag_to_movie.bash
```
