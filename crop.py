import cv2
import os

"""
Function below split videos into a frames. 
For loop iterating through the all video files in directory.
While loop inside a for loop splitting images into a frames.
"""


def frame_video():
    directory_videos = '/home/lab/PycharmProjects/filmy_przyciete/'
    directory_frames = '/home/lab/PycharmProjects/nagrania_frames/'
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
    directory = '/home/lab/PycharmProjects/nagrania_frames/'
    dir = os.listdir(directory)
    x, y, h, w = 160, 80, 650, 1090  # set coordinates that you want

    for index_lista, name in enumerate(dir):
        if index_lista % 5 == 0:
            # print(index_lista)
            img = cv2.imread(directory + name)
            crop_img = img[y:h, x:w]
            cv2.imwrite('/home/lab/PycharmProjects/cropped/' + name, crop_img)


def delete_files():
    directory = '/home/lab/PycharmProjects/nagrania_frames/'

    for file in os.listdir(directory):
        os.remove(directory + file)


print('Start split video into a frames. . .')
frame_video()
print('Start cropping. . .')
crop_image()
print('Delete files. . .')
delete_files()
print('DONE!')
