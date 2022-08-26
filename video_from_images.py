import cv2
import numpy as np
import os


def create_video():
    directory = r"C:\Users\Krystian\Desktop\val_copy"
    video_name = r"C:\Users\Krystian\Desktop\val_copy\video3_fps.avi"

    images = [img for img in os.listdir(directory) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(directory, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 3, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(directory, image)))

    cv2.destroyAllWindows()
    video.release()


create_video()
