# import modules
from PIL import Image, ImageColor, ImageOps
import requests as res
from io import BytesIO as byio
from time import sleep
import re, sys
import numpy as np
def getImage(): 
    link = input('Please enter a url to an image: ')  
    if link == 'local':
        try:
            img = Image.open('image.png')
            img.save('past.png')
            return
        except Exception as E:
            print(f'An exception occured: {E}.')
            sleep(7)
            sys.exit()
    r = res.get(link)
    img = Image.open(byio(r.content))
    img.save('past.png')
def inputcolor():
    img = Image.open('past.png')
    img = img.convert('RGB')
    targetcolor = input('What color do you want to search for, you can use RGB format or common names like \'red\', \'black\', e.t.c. Leave this blank to invert all pixels. ')
    print('Processing image. This could take several minutes.')
    isrgb = re.match(r'\d+, \d+, \d+|\(\d+, \d+, \d+\)', targetcolor)
    if type(isrgb) == re.Match:
        targetcolor = targetcolor.strip('()')
        targetcolor = targetcolor.split(', ')
        targetcolor = tuple(map(int, targetcolor))
        print(str(targetcolor))
    else:
        try:
            targetcolor = ImageColor.getcolor(targetcolor.lower(), 'RGB')
            print(targetcolor)
        except:
            if targetcolor != '':
                print('Not a valid color smh.')

    return targetcolor
def invertimage():
    img = Image.open('past.png')
    if targetcolor == '':
        invertimage = ImageOps.invert(img)
        invertimage.save('result.png')
        invertimage.show()
        sys.exit()
    invertimage = img.copy().convert('RGB')
    invertimage = ImageOps.invert(invertimage)
    invertimage.save('invert.png')
    pastarray = np.array(img)
    targetcolorarray = np.array(targetcolor)
    inverse = np.array(invertimage)
    result = np.where((pastarray==targetcolorarray).all(axis=-1)[...,None], inverse, pastarray)
    Image.fromarray(result.astype(np.uint8)).save('result.png')
try:
    getImage()
except:
    raise Exception('Image not found. Please double-check the url.')
targetcolor = inputcolor()
invertimage()