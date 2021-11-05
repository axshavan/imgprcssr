#!/bin/python
import sys
from PIL import Image
import filters

if len(sys.argv) < 3:
    print("Usage: run.py <image> [<command[,param1[,...]]> [...]]")
    exit(0)

try:
    image = Image.open(sys.argv[1])
except Exception as e:
    print("Cannot open image " + sys.argv[1] + ": " + str(e))
    exit(0)

# load image data
processing_image_data = []
row = []
for x in range(image.width):
    row = []
    for y in range(image.height):
        pixel = image.getpixel((x, y))
        row.append([float(pixel[0]), float(pixel[1]), float(pixel[2])])
    processing_image_data.append(row)

# pipeline image filters
row = 0
for i in sys.argv:
    if row > 1:
        f = i.split(',')
        if hasattr(filters, 'filter_' + f[0]):
            f[0] = getattr(filters, 'filter_' + f[0])
            try:
                processing_image_data = f[0](processing_image_data, f[1:] if len(f) > 1 else [])
            except Exception as e:
                print("Cannot apply filter " + f[0] + ": " + str(e))
        else:
            print(f[0] + " is unknown filter")
    row += 1

# save image
for x in range(image.width):
    for y in range(image.height):
        image.putpixel((x, y), (
            int(processing_image_data[x][y][0]),
            int(processing_image_data[x][y][1]),
            int(processing_image_data[x][y][2])
        ))
    row = 0
image.save('out_' + sys.argv[1])
