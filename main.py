import cv2

cap = cv2.VideoCapture('FLIR1234.mp4')

cnt = 0

w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

x, y, h, w = 70, 75, 695, 995

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('result.avi', fourcc, fps, (w, h))

while cap.isOpened():
    ret, frame = cap.read()

    cnt += 1  # Counting frames

    # Avoid problems when video finish
    if ret:
        # Cropping the frame
        crop_frame = frame[y:h, x:w]

        # Percentage
        xx = cnt * 100 / frames
        print(int(xx), '%')

        # Saving from the desired frames
        #if 15 <= cnt <= 90:
        #    out.write(crop_frame)

        # I see the answer now. Here you save all the video
        out.write(crop_frame)

        # Just to see the video in real time
        cv2.imshow('cropped', crop_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
