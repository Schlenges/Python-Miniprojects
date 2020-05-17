import sys
import os
from PIL import Image, UnidentifiedImageError

def _trim(filename):
  trimmed = os.path.splitext(filename)[0].split('/')[-1]
  return trimmed

def _convert(file_path, output_path):
  img = Image.open(file_path)
  output_path = f'{output_path}/{_trim(file_path)}'
  img.save(f'{output_path}.png', 'png')
  print(f'{file_path} converted')

def run(jpg_path, png_path):
  if not os.path.exists(png_path):
    os.makedirs(png_path)

  if os.path.isdir(jpg_path):
    for filename in os.listdir(jpg_path):
      try:
        _convert(f'{jpg_path}/{filename}', png_path)
      except UnidentifiedImageError:
        continue
  elif os.path.isfile(jpg_path):
    try:
      _convert(jpg_path, png_path)
    except UnidentifiedImageError:
      print('file is not an image')
  else:
    print('please enter a valid input file path')

def main(args):
  try:
    jpg_path = args[1]
    png_path = args[2]
    run(jpg_path, png_path)
  except IndexError:
    print('please enter an input and output path')
    sys.exit()

main(sys.argv[:3])