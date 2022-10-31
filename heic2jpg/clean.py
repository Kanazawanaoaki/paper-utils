# coding: utf-8
from PIL import Image
import pyheif
import pathlib
import glob
import os


# 削除対象のファイルがあるディレクトリ
heic_dir = pathlib.Path('./heic')
jpg_dir = pathlib.Path('./jpg')
# globでディレクトリ内のHEICファイルをリストで取得
heic_image_path = list(heic_dir.glob('**/*.HEIC'))
jpg_image_path = list(jpg_dir.glob('**/*.jpg'))
image_path = heic_image_path + jpg_image_path

# リストの画像ファイルを１個づつ削除
for i in image_path:
    os.remove(i)
    print("{} is deleted".format(i))
