# Image Cropper for Samsung TV Frame Art Mode #

A [Samsung TV](https://www.samsung.com/us/televisions-home-theater/tvs/the-frame/65-the-frame-qled-4k-smart-tv-2021-qn65ls03aafxza/) that supports "Art Mode" requires images to be in the aspect ratio 16:9.

This script will crop images in the specified folder with the specified aspect ratio (or default 16:9 if none provided).

## How to run the script ##

Here is an example:

`python3 crop-images.py --input=/path/to/folder_with_images/`

## Options ##

### -i, --input ###

Input folder. The script should support folder with many images folders inside. 

### -a, --aspect ###

Specify an aspect ratio if needed in the format `16:9`. Optional, default value 16:9.

### -b, --border_crop ###

Specify a number to cut from all sides of the images should you need to.

### -o, --output ###
Speify an output location if needed. Otherwise will create in the script directory in the format `output_images_datetime`


# How To Add Your Own Art to Samsung TV Frame #
1. Download Samsung’s free SmartThing App ([iOS](https://apps.apple.com/us/app/smartthings/id1222822904) / [Android](https://play.google.com/store/apps/details?id=com.samsung.android.oneconnect&hl=en_US&gl=US)) and connect it to your TV.
2. The key to adding your own art is to make sure you have the exact ratio set of 16:9 or 3840 x 2160 pixels.
3. Within the app, select Art Mode.
4. Add your art downloads or photos.
