# coding: utf-8
from PIL import Image
import pyheif
import pathlib
import glob


def heic_png(image_path, save_path):
    # HEICファイルpyheifで読み込み
    heif_file = pyheif.read(image_path)
    # 読み込んだファイルの中身をdata変数へ
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    # JPEGで保存
    data.save(str(save_path), "JPEG")


# 変換対象のファイルがあるディレクトリ
# カレントの下のtempディレクトリを指定
image_dir = pathlib.Path('./heic')
# globでディレクトリ内のHEICファイルをリストで取得
heic_path = list(image_dir.glob('**/*.HEIC'))

# リストのHEICファイルを１個づつJPEGへ変換
for i in heic_path:
    m = "./" + str(i)
    n = './jpg/' + str(i.stem) + '.jpg'
    heic_png(m, n)
    print("{} is converted to {}".format(m,n))
