import conv
import setup
import cv2

# print all sources to convert
count=0
for i in setup.imgs:
    print(i)
    cv2.imwrite('./out/out_{}.jpg'.format(count),conv.convert(cv2.imread(i)))
    count+=1;

for i in setup.vids:
    print(i)
