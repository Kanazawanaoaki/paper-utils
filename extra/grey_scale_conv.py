import cv2

import sys

path_r = "0s_cropped_prosilica.jpg"
path_w = "0s_cropped_prosilica_grey.jpg"

if len(sys.argv)>=2:
    path_r = sys.argv[1]
    if len(sys.argv)>=3:
        path_w = sys.argv[2]

im_gray = cv2.imread(path_r,cv2.IMREAD_GRAYSCALE)
cv2.imwrite(path_w, im_gray)
