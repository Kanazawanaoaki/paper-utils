import cv2
import argparse

parser = argparse.ArgumentParser(description='grey scale converter')
parser.add_argument('-r', '--raw', default="0s_cropped_prosilica.jpg")
parser.add_argument('-g', '--grey', default="0s_cropped_prosilica_grey.jpg")
args = parser.parse_args()

path_r = args.raw
path_w = args.grey

im_gray = cv2.imread(path_r,cv2.IMREAD_GRAYSCALE)
cv2.imwrite(path_w, im_gray)
