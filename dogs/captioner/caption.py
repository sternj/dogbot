from dogs.captioner.image_getter import get_random_image
from dogs.captioner.joke_getter import get_joke_of_right_length
from PIL import ImageDraw, Image, ImageFont, ImageStat
from typing import List

def put_text(use_bottom):
    img = get_random_image()
    joke = get_joke_of_right_length()
    write_on_image(img, joke, use_bottom=use_bottom)
    return img

def write_on_image(image: Image, text: List[str], use_bottom=True):
    top, bottom = text
    fontSize = int(image.size[1]/5)
    font, topsize, bottomsize = update_font(fontSize, top, bottom)
    while topsize > image.size[0] - 20 or (bottomsize > image.size[0] - 20 and use_bottom):
        fontSize -= 1
        font, topsize, bottomsize = update_font(fontSize, top, bottom)
    color = (0,0,0)
    if brightness(image) < 130:
        color = (255, 255, 255)
    draw = ImageDraw.Draw(image)
    draw.text((image.size[0] / 2 - topsize / 2,10), top, font=font, fill=color)
    if use_bottom:
        draw.text((image.size[0]/2 - bottomsize / 2, image.size[1]-10-fontSize), bottom, font=font, fill=color)

def update_font(fontsize, top, bottom):
    font = ImageFont.truetype("./Impact.ttf", fontsize)
    topSize = font.getsize(top)
    bottomSize = font.getsize(bottom)
    return font, topSize[0], bottomSize[0]

def brightness(image):
   im = image.convert('L')
   stat = ImageStat.Stat(im)
   return stat.rms[0]