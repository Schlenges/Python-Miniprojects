import sys
import os
from PIL import Image, UnidentifiedImageError


def _clean_filename(file_path):
    filename = os.path.splitext(file_path)[0].split('/')[-1]
    return filename


def _convert(file_path, output_dir, img_format="png"):
    img = Image.open(file_path)
    output_path = f'{output_dir}/{_clean_filename(file_path)}.{img_format}'
    img.save(output_path, img_format)
    print(f'{file_path} converted')


def run(jpg_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.isdir(jpg_path):
        for filename in os.listdir(jpg_path):
            try:
                _convert(f'{jpg_path}/{filename}', output_dir)
            except UnidentifiedImageError:
                continue
    elif os.path.isfile(jpg_path):
        try:
            _convert(jpg_path, output_dir)
        except UnidentifiedImageError:
            print('file is not an image')
    else:
        print('please enter a valid input file path')


def main(args):
    try:
        jpg_path = args[1]
        output_dir = args[2]
        run(jpg_path, output_dir)
    except IndexError:
        sys.exit('please enter an input and output path')


main(sys.argv[:3])
