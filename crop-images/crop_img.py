import cv2
import sys

path = "carrot-rotate-peel-kinect/pr2_kinect_after_peel.png"
path2 = "carrot-rotate-peel-kinect/pr2_kinect_after_peel.png"
if len(sys.argv)>=2:
    path = sys.argv[1]
    if len(sys.argv)>=2:
        path2 = sys.argv[2]
        
im = cv2.imread(path)
h,w,ch = im.shape

y_num = int(round(h/32))*19
y_size = 120
x_num = int(round(h/32))*19
x_size = 90

im_cropped = im[x_num:x_num+x_size , y_num:y_num+y_size, :]

cv2.imwrite(path2, im_cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print(im_cropped.shape)

