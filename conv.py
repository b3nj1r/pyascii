import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw

# frame conversion algorithm
print("conv.py name:", __name__)

# scale factor
scale = 15
# dimensions of a character in pixels
psi = 15

# perceived brightness color values
pr = 0.299
pg = 0.587
pb = 0.114

def convert(im):
    # calculate image scale factor
    dsize = int(im.shape[1] * scale / 100), int(im.shape[0] * scale / 100)
    owi, ohi = dsize[0]*psi,dsize[1]*psi

    # resize image contents for faster compute
    rdc = cv2.resize(im, dsize)
    rdc = np.array(rdc).astype(np.uint8)

    # initialize output frames
    img = Image.fromarray(cv2.resize(rdc, (owi, ohi), interpolation=cv2.INTER_NEAREST))
    dw = ImageDraw.Draw(img)

    # compute here
    y = 0
    for r in rdc:
        x = 0
        for c in r:
            # chose from a range of 16 characters using the luminance as index
            xtext = ' .,:ilwnmWNM68@#'[int(pr * c[0] + pg * c[1] + pb * c[2]) // 16]
            # np.array(c).clip(96,128)

            # write text to image
            dw.text((x, y), xtext, (int((c[0] // 2) ** 1.3), int((c[1] // 2) ** 1.4), int((c[2] // 2) ** 1.5)), ImageFont.truetype('LucidaTypewriterRegular.ttf', psi))
            x += psi
        y += psi
    return np.array(img)

