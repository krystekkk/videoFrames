import cv2
import os

"""
Function below split videos into a frames. 
For loop iterating through the all video files in directory.
While loop inside a for loop splitting images into a frames.
"""


def frame_video():
    directory_videos = '/home/lab/PycharmProjects/nagrania/'
    directory_frames = '/home/lab/PycharmProjects/nagrania_frames/'
    count = 0

    for video in os.listdir(directory_videos):
        video = cv2.VideoCapture(directory_videos + video)
        success, image = video.read()

        while success:
            cv2.imwrite(directory_frames + 'frame%d.png' % count, image)
            success, image = video.read()
            print('Read a new frame: ', success)
            count += 1


    # vidcap = cv2.VideoCapture('FLIR1234.mp4')
    # success, image = vidcap.read()
    # # count = 0
    #
    # while success:
    #     cv2.imwrite('/home/lab/PycharmProjects/frames/frame%d.jpg' % count, image)  # save frame as JPEG file
    #     success, image = vidcap.read()
    #     print('Read a new frame: ', success)
    #     count += 1


def crop_image():
    directory = '/home/lab/PycharmProjects/nagrania_frames/'
    x, y, h, w = 70, 75, 695, 995  # set coordinates that you want

    for files in os.listdir(directory):
        img = cv2.imread(directory + files)
        crop_img = img[y:h, x:w]
        cv2.imwrite('/home/lab/PycharmProjects/cropped/' + files, crop_img)
        print(f'Cropped file: {files}')


print('Start split video into a frames. . .')
frame_video()
print('Start cropping. . .')
crop_image()
print('COMPLETED!')
