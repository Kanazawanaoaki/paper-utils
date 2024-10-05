#!/usr/bin/env python3

import argparse
import os
import re
import cv2

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def create_video_from_images(image_folder, output_path, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort(key=natural_keys)

    if not images:
        print("No images found in the specified folder.")
        return

    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    print(f"Video saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a video from images in a specified folder.')
    parser.add_argument('--image_folder', '-i', default='/home/kanazawa/Downloads/20240614_tracking_test/20240607_kitchen_bag_10_onion/rgb/', type=str, help='Path to the folder containing images')
    parser.add_argument('--output_path', '-o', default='/home/kanazawa/Downloads/20240614_tracking_test/20240607_kitchen_bag_10_onion/20240607_kitchen_bag_10_onion.mp4', type=str, help='Path to save the output video')
    parser.add_argument('--fps', type=int, default=10, help='Frames per second for the output video')

    args = parser.parse_args()

    print("video fps is specifed in {}".format(args.fps))
    create_video_from_images(args.image_folder, args.output_path, args.fps)
