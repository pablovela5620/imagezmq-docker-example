import cv2
import imagezmq
from imutils.video import VideoStream

cam = VideoStream().start()

while True:  # show streamed images until Ctrl-C
    image = cam.read()
    cv2.imshow('video', image)  # 1 window for each RPi
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break