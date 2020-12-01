import conv
import setup
import cv2


# scale factor
scale = 5
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
    cv2.imwrite('./out/out_{}.jpg'.format(count),conv.convert(cv2.imread(i),scale,psi,pr,pg,pb))
    count+=1;

count=0

for i in setup.vids:
    # video capture
    cap = cv2.VideoCapture(i)

    # output width and height
    owi = int(cap.get(3) * (scale / 100) * psi)
    ohi = int(cap.get(4) * (scale / 100) * psi)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # output file
    out = cv2.VideoWriter('./out/out_{}.avi'.format(count),cv2.VideoWriter_fourcc(*'XVID'), 24, (owi, ohi))
    frame_count=0
    percentage=0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(conv.convert(frame,scale,psi,pr,pg,pb))
            print('file | {}\n'.format(i))
            print('#'*(percentage//2)+'.'*((100//2) - (percentage//2))
        frame_count+=1
        # print(frame_count)
        percentage = int((frame_count/length)*100)
        if not ret:
            break
    # release if successful
    out.release()
    cap.release()

    # print(i)
    count+=1
