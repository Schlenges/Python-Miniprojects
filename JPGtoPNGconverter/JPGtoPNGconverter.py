import sys
import os
from PIL import Image, UnidentifiedImageError

input_path = sys.argv[1]
output_path = sys.argv[2]

def _trim(filename):
  trimmed = os.path.splitext(filename)[0].split('/')[-1]
  return trimmed

def _convert(input, output):
  img = Image.open(input)
  img.save(f'{output}.png', 'png')
  print(f'{input} converted')


if not os.path.exists(output_path):
  os.makedirs(output_path)

if os.path.isdir(input_path):
  for filename in os.listdir(input_path):
    try:
      input_file = f'{input_path}/{filename}'
      output_file = f'{output_path}/{_trim(filename)}'
      _convert(input_file, output_file)
    except UnidentifiedImageError:
      continue
elif os.path.isfile(input_path):
  try:
    input_file = f'{input_path}'
    output_file = f'{output_path}/{_trim(input_path)}'
    _convert(input_file, output_file)
  except UnidentifiedImageError:
    print('file is not an image')
else:
  print('please enter a valid input file path')
