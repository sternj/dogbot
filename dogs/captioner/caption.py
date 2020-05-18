from dogs.captioner.image_getter import get_random_image
from dogs.captioner.joke_getter import get_joke_of_right_length
from PIL import ImageDraw, Image, ImageFont, ImageStat
from typing import List

def put_text(use_bottom):
    img = get_random_image()
    joke = get_joke_of_right_length()
    write_on_image(img, joke, use_bottom=use_bottom)
    return img

# These next two functions are roughly based on lines 19-35 of this file:
# https://github.com/danieldiekmeier/memegenerator/blob/master/memegenerator.py
# 
# I did some slight restructuring because I wasn't satisfied with that long while loop
def write_on_image(image: Image, text: List[str], use_bottom=True, strokewidth=2):
    top, bottom = text
    fontSize = int(image.size[1]/5)
    font, topsize, bottomsize = update_font(fontSize, top, bottom, strokewidth)
    while topsize > image.size[0] - 20 or (bottomsize > image.size[0] - 20 and use_bottom):
        fontSize -= 1
        font, topsize, bottomsize = update_font(fontSize, top, bottom, strokewidth)
    color = (255, 255, 255)
    draw = ImageDraw.Draw(image)
    draw.text((image.size[0] / 2 - topsize / 2,10), top, font=font, fill=color, stroke_width=strokewidth, stroke_fill=(0,0,0))
    if use_bottom:
        draw.text((image.size[0]/2 - bottomsize / 2, image.size[1]-10-fontSize), bottom, font=font, fill=color, stroke_width=strokewidth, stroke_fill=(0,0,0))

def update_font(fontsize, top, bottom, strokewidth):
    # Unfortunately, based on these docs https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html#methods,
    # there's no way to pre-cache this file to reduce loads from the filesystem
    # or to resize this font
    font = ImageFont.truetype("./Impact.ttf", fontsize)
    topSize = font.getsize(top, stroke_width=strokewidth)
    bottomSize = font.getsize(bottom, stroke_width=strokewidth)
    return font, topSize[0], bottomSize[0]
