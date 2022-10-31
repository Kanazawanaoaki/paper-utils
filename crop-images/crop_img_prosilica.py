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

num = 350
x_num = int(round(w/32))*6
y_num = int(round(h/32))*4
x_size = 4 * num
y_size = 3 * num

im_cropped = im[y_num:y_num+y_size, x_num:x_num+x_size, :]

cv2.imwrite(path2, im_cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print(im_cropped.shape)

