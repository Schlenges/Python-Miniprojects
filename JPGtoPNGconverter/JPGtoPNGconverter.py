import sys
import os
from PIL import Image, UnidentifiedImageError

input_path = sys.argv[1]
output_path = sys.argv[2]

if not os.path.exists(output_path):
  os.makedirs(output_path)

if os.path.isdir(input_path):
  for filename in os.listdir(input_path):
    try:
      img = Image.open(f'{input_path}/{filename}')
      clean_filename = os.path.splitext(filename)[0]
      img.save(f'{output_path}/{clean_filename}.png', 'png')
      print(f'{filename} converted')
    except UnidentifiedImageError:
      continue

if os.path.isfile(input_path):
  try:
      img = Image.open(f'{input_path}')
      clean_filename = os.path.splitext(input_path)[0]
      clean_filename = clean_filename.split('/')[-1]
      img.save(f'{output_path}/{clean_filename}.png', 'png')
      print(f'{input_path} converted')
  except UnidentifiedImageError:
    print('file is not an image')
