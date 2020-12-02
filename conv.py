import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw

# frame conversion algorithm
print("conv.py name:", __name__)

def convert(im, scale, psi, pr, pg, pb,owi,ohi):
    # calculate image scale factor
        dsize = int(im.shape[1] * scale / 100), int(im.shape[0] * scale / 100)
        rdc = cv2.resize(im, dsize)
        rdc = np.array(rdc).astype(np.uint8)

        # initialize output frames
        img = Image.fromarray(cv2.resize(rdc, (owi, ohi), interpolation=cv2.INTER_NEAREST))
        dw = ImageDraw.Draw(img)
        # compute here
        y = 0
        for r in rdc:
            # iterate rows
            x = 0
            for c in r:
                # iterate columns
                xtext = ' .,:ilwnmWNM68@#'[int(pr * c[0] + pg * c[1] + pb * c[2]) // 16]
                # np.array(c).clip(96,128)
                dw.text((x, y), xtext, (int((c[0] // 2) ** 1.3), int((c[1] // 2) ** 1.4), int((c[2] // 2) ** 1.5)),
                        ImageFont.truetype('lucida_typewriter_regular.ttf', psi))
                x += psi
            y += psi
        return (np.array(img))