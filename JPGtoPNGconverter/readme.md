# JPG to PNG Converter
A simple Python 3 script using [Pillow](https://pypi.org/project/Pillow/) to convert jpg images to png. The script will either convert a single image, or loop over all images in the input folder and save the converted images to the given output directory. If the output directory doesn't exist, the program will create it for you.

## Usage:
Run the script by providing the path to the **image** or the **image folder** as the first argument, and the path of the **output folder** as the second.
```bash
$ python3 JPGtoPNGconverter.py ./jpg ./png
```  
You may have to run the program with superuser privileges (i.e. sudo).