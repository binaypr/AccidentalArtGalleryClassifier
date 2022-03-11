import os
import pathlib
from statistics import median
from turtle import width
import PIL
import PIL.Image as Image
import glob





PIL.Image.MAX_IMAGE_PIXELS = 93312000

dir = "C:\\Users\\rijal\\Downloads\\wikiart\\wikiart"

files = glob.glob(dir + '/**/*.jpg', recursive=True)

width = []
height = []

counter = 0



for file in files:
    counter += 1
    if(counter % 100 == 0):
        print(">", end="", flush=True)


    try:
        w, h = Image.open(file).size
        width.append(w)
        height.append(h)
    except Exception as e:
        print(file)
        continue

print(median(width))
print(median(height))
print(counter)

