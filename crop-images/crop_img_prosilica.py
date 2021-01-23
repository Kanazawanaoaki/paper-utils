import cv2
import sys

path = "carrot-rotate-peel-kinect/pr2_kinect_after_peel.png"
path2 = "carrot-rotate-peel-kinect/pr2_kinect_after_peel.png"
if len(sys.argv)>=2:
    path = sys.argv[1]
    if len(sys.argv)>=3:
        path2 = sys.argv[2]
        
im = cv2.imread(path)
h,w,ch = im.shape

print(h,w)

x_num = int(round(h/32))*9
# x_size = 720
x_size = 900
y_num = int(round(w/32))*3
# y_size = 960
y_size = 1200

im_cropped = im[x_num:x_num+x_size , y_num:y_num+y_size, :]

cv2.imwrite(path2, im_cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print(im_cropped.shape)

