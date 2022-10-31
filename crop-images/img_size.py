import cv2
import argparse

parser = argparse.ArgumentParser(description='grey scale converter')
parser.add_argument('-o', '--original', default="carrot-rotate-peel-kinect/pr2_kinect_after_peel.png")
args = parser.parse_args()

path = args.original

im = cv2.imread(path)
print(im.shape)

