import os
import re
import inspect
import subprocess
import sys
import getopt
from typing import List
from datetime import datetime
from PIL import Image

def crop_files(folder: str, output_folder: str, required_aspect: int, border: int):
    str_dt = str(datetime.now())
    output_folder = output_folder if output_folder.endswith("/") else output_folder + "/"
    print('{} Going through your files in the input folder'.format(str_dt))
    for (root, dirs, files) in sorted(os.walk(folder), key=lambda tup: tup[0].lower()):
        for file in files:
            print(".", end="", flush=True)  # Indicates progress
            try:
                image = Image.open(root + "/" + file)
            except Exception as error:
                print('\n' + str(error))
                continue

            width = image.size[0]
            height = image.size[1]
            aspect = width / height

            if aspect > required_aspect:
                # Then crop the left and right edges:
                new_width = int(required_aspect * height)
                offset = int(abs(width - new_width) / 2)
                resize = (offset + border, border, width - offset - border, height - border)
            else:
                # crop the top and bottom:
                new_height = int(width / required_aspect)
                offset = int(abs(height - new_height))
                resize = (border, border, width - border, height - offset - border)

            cropped_image = image.crop(resize)
            cropped_image.save(output_folder + str_dt + "_" + file)

def main(argv):
    print('\n\n{} Checking your arguments...'.format(str(datetime.now())))

    opts, args = getopt.getopt(argv, "i:o:a:b", ["input=", "output=", "aspect=", "border_crop="])
    folder = None
    output_folder = None
    aspect = "16:9"
    border = 0
    for opt, arg in opts:
        if opt in ("--input", "-i"):
            folder = arg
        if opt in ("--output", "-o"):
            output_folder = arg
        if opt in ("--aspect", "-a"):
            aspect = arg
        if opt in ("--border_crop", "-b"):
            border = int(arg)

    if not os.path.exists(folder):
        print("No input folder found")
        return

    if output_folder is None:
        current_script_location = inspect.getfile(inspect.currentframe())
        current_dir_location = os.path.dirname(os.path.abspath(current_script_location))
        output_folder = current_dir_location + "/output_images_" + str(datetime.now())

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    aspect_ratio = int(aspect.split(':')[0]) / int(aspect.split(':')[1])
    
    crop_files(folder, output_folder, aspect_ratio, border)

    print('\n{} All done. Files saved into {}\n\n'.format(str(datetime.now()), output_folder))


if __name__ == "__main__":
    main(sys.argv[1:])
