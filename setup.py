import glob
# prepare image or video frames for conversion
print("setup.py name:", __name__)

# accepted image file extensions
image_formats = ['png','jpg','jpeg','jpe','tiff','tif']
# accepted video file extensions
video_formats = ['mp4','avi']
imgs,vids = [], []

# iterate over all image formats
for mat in image_formats:
    # print(mat)
    imgs += glob.glob('./in/*.'+mat)

# iterate over all video formats
for mat in video_formats:
    # print(mat)
    vids += glob.glob('./in/*.'+mat)
