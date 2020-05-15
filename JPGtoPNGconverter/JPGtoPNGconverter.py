import sys
import os
from PIL import Image, UnidentifiedImageError

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

for filename in os.listdir(image_folder):
  try:
    img = Image.open(f'{image_folder}/{filename}')
    clean_filename = os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{clean_filename}.png', 'png')
    print(f'{filename} converted')
  except UnidentifiedImageError:
    continue

