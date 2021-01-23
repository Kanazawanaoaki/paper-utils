import cv2
import sys

path = "carrot-rotate-peel-kinect/pr2_kinect_after_peel.png"
path2 = "carrot-rotate-peel-kinect/pr2_kinect_after_peel.png"
if len(sys.argv)>=2:
    path = sys.argv[1]
    if len(sys.argv)>=3:
        path2 = sys.argv[2]
        
im = cv2.imread(path)
print(im.shape)

