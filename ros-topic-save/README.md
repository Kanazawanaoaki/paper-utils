# ROS topic save
ROSトピックの保存方法についてメモなど．

## data collection server
data collection serverを使う．サンプルのlaunchがある．

## image topic save
```
rosrun image_view image_saver image:=/camera/rgb/image_raw save_all_image:=false __name:=image_saver
```

comp
```
cd scripts
python comp_rosbag_to_movie.py -b bags/ -d movies/
```
or
```
bash comp_rosbag_to_movie.bash
```