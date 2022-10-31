import cv2
import argparse

parser = argparse.ArgumentParser(description='grey scale converter')
parser.add_argument('-o', '--original', default="carrot-rotate-peel-kinect/pr2_kinect_after_peel.png")
parser.add_argument('-c', '--cropped', default="carrot-rotate-peel-kinect/pr2_kinect_after_peel.png")
args = parser.parse_args()

path = args.original
path2 = args.cropped

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

