#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, sys
import rosbag
import matplotlib.pyplot as plt
import moviepy.editor as mpy
import math
import csv
import pickle
import numpy as np

from cv_bridge import CvBridge, CvBridgeError
import cv2
from PIL import Image



class RosbagReader(object):
    def __init__(self,bag_dir,data_dir):
        self.bag_dir = bag_dir
        self.data_dir = data_dir
        print("bag_dir : {}, data_dir : {}".format(self.bag_dir,self.data_dir))
        self.check_and_make_dir(self.data_dir)
        self.load_rosbag()        

    def check_and_make_dir(self,dir_path):
        if False == os.path.exists(dir_path):
            os.makedirs(dir_path)
            print("make dir in path: {}".format(dir_path))

    def save_video(self,frames, path):
        clip = mpy.ImageSequenceClip(frames, fps=30)
        clip.write_videofile(path, fps=30)
        
    def load_rosbag(self):
        bag_files = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/' + self.bag_dir +'*.bag')
        print(bag_files)

        img_list = []
        bridge = CvBridge()
        for file_name in bag_files:
            bag = rosbag.Bag(file_name)

            # bag_save_path = self.data_dir+str(file_name[file_name.rfind('/')+1:])+"/"
            # self.check_and_make_dir(bag_save_dir)
            bag_img_list = [] 
            
            for topic, msg, t in bag.read_messages():
                if topic == "/kinect_head/rgb/image_rect_color/compressed":
                    t = msg.header.stamp
                    time = t.secs + 1e-9 * t.nsecs
                    
                    # 画像の保存 listに追加と画像でも保存．
                    img = bridge.compressed_imgmsg_to_cv2(msg)
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # pil_img = Image.fromarray(img_rgb)
                    # img_np = np.array(img_rgb)
                    bag_img_list.append(img_rgb)
                    
            # data saves
            movie_file = self.data_dir+str(file_name[file_name.rfind('/')+1:file_name.rfind('.')])+".mp4"
            self.save_video(bag_img_list, movie_file)
            print("image also saved in {}".format(movie_file))
            
if __name__ == '__main__':
    bag_dir = sys.argv[sys.argv.index("-b") + 1] if "-b" in sys.argv else '../../bags/'
    if bag_dir[-1:] != '/':
        bag_dir += '/'
    data_dir = sys.argv[sys.argv.index("-d") + 1] if "-d" in sys.argv else '../data/from_rosbag/'
    if data_dir[-1:] != '/':
        data_dir += '/'
    reader=RosbagReader(bag_dir,data_dir)
