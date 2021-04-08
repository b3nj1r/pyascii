import conv
import setup
import cv2
import numpy as np
# scale factor
scale = int(input("enter scale factor of the resulting files: "))
# dimensions of a character in pixels
psi = 15

# perceived brightness color values
pr = 0.299
pg = 0.587
pb = 0.114

# print all sources to convert
count=0

for i in setup.imgs:
    # print(i)
    cv2.imwrite('./out/out_{}.jpg'.format(count),conv.convert(cv2.imread(i),scale,psi,pr,pg,pb,cv2.imread(i).shape[1],cv2.imread(i).shape[1]))
    count+=1;

count=0

for i in setup.vids:
    # read source video
    cap = cv2.VideoCapture(i)
    # output width, output height
    owi, ohi = int(cap.get(3) * (scale / 100) * psi), int(cap.get(4) * (scale / 100) * psi)
    # initialize output video
    out = cv2.VideoWriter('./out/out.mp4{}'.format(count), cv2.VideoWriter_fourcc(*'mp4v'), 32, (owi, ohi))
    if not cap.isOpened():
        print('read error')
    i = 0
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    percentage=0
    frame_count=0

    # frame handle
    while cap.isOpened:
        ret, frm = cap.read()
        if not ret:
            # conclude loop when video terminates
            break
        if frame_count%6==0:
            frame = np.array(conv.convert(frm,scale,psi,pr,pg,pb,owi,ohi))
        cv2.imshow('frame',frm)
        out.write(frame)
        print('file | {}\n'.format(i))
        print('#'*(percentage//2)+'.'*((100//2) - (percentage//2)))
        frame_count+=1
        # print(frame_count)
        percentage = int((frame_count/length)*100)
        if cv2.waitKey(1) == ord('q'):
            break

    # release if successful
    out.release()
    cap.release()

    # print(i)
    count+=1
