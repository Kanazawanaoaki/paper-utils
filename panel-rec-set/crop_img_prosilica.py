import cv2
import sys

path_r = "ih-panel-off.png"
path_w = "ih-panel-off-cropped.jpg"

if len(sys.argv)>=2:
    path_r = sys.argv[1]
    if len(sys.argv)>=3:
        path_w = sys.argv[2]
    
im = cv2.imread(path_r)
h,w,ch = im.shape

x_start = int(round(h/32))*11+50
x_size = 120
y_start = int(round(w/32))*11+10
y_size = 180

im_cropped = im[x_start:x_start+x_size , y_start:y_start+y_size, :]

cv2.imwrite(path_w, im_cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print(im_cropped.shape)

