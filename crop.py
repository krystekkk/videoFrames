import cv2
import os

"""
Function below split videos into a frames. 
For loop iterating through the all video files in directory.
While loop inside a for loop splitting images into a frames.
"""


def frame_video():
    directory_videos = 'C:/Users/Krystian/Desktop/crop_process/nagrania/'
    directory_frames = 'C:/Users/Krystian/Desktop/crop_process/nagrania_frames/'
    count = 0

    for video in os.listdir(directory_videos):
        video = cv2.VideoCapture(directory_videos + video)
        success, image = video.read()

        while success:
            cv2.imwrite(directory_frames + 'frame%d.png' % count, image)
            success, image = video.read()
            # print('Read a new frame: ', success)
            count += 1


def crop_image():
    directory_source = 'C:/Users/Krystian/Desktop/crop_process/nagrania_frames/'
    x, y, h, w = 70, 75, 695, 995  # set coordinates that you want

    for files in os.listdir(directory_source):
        img = cv2.imread(directory_source + files)
        crop_img = img[y:h, x:w]
        cv2.imwrite('C:/Users/Krystian/Desktop/crop_process/cropped/' + files, crop_img)
        print(f'Cropped file: {files}')
    print('Crop - done.')

# print('Start split video into a frames. . .')
# frame_video()
print('Start cropping. . .')
crop_image()
print('COMPLETED!')
