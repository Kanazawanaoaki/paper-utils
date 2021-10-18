import cv2
import sys

path = "carrot-rotate-peel-kinect/pr2_kinect_before_peel_01.png"
if len(sys.argv)>=2:
    path = sys.argv[1]

img = cv2.imread(path)
print(img.shape)

