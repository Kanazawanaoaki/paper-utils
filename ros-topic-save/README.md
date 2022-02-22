# ROS topic save
ROSトピックの保存方法についてメモなど．

## data collection server
data collection serverを使う．サンプルのlaunchがある．

## image topic save
```
rosrun image_view image_saver image:=/camera/rgb/image_raw save_all_image:=false __name:=image_saver
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
