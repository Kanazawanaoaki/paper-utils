# coding: utf-8
from PIL import Image
import pillow_heif
import pathlib

# HEIC を Pillow で扱えるよう登録
pillow_heif.register_heif_opener()

def heic_to_jpg(image_path, save_path):
    with Image.open(image_path) as img:
        rgb = img.convert("RGB")
        rgb.save(save_path, "JPEG", quality=95)

if __name__ == "__main__":
    image_dir = pathlib.Path('./heic')
    out_dir   = pathlib.Path('./jpg')
    out_dir.mkdir(exist_ok=True)
    for heic in image_dir.glob('**/*.HEIC'):
        jpg_path = out_dir / (heic.stem + '.jpg')
        heic_to_jpg(str(heic), str(jpg_path))
        print(f"{heic} → {jpg_path}")
