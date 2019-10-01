import sys
sys.path.insert(0, '/Users/pablo/0Dev/repos/imagezmq/imagezmq')  # imagezmq.py is in ../imagezmq

import socket
import time
import cv2
import imutils
from imutils.video import VideoStream
import os
import imagezmq

# use either of the formats below to specifiy address of display computer
# sender = imagezmq.ImageSender(connect_to='tcp://jeff-macbook:5555')
address = os.environ["ZMQ_ADDRESS"]
sender = imagezmq.ImageSender(connect_to=address)

picam = VideoStream().start()
time.sleep(1.0)  # allow camera sensor to warm up
while True:  # send images as stream until Ctrl-C
    image = picam.read()
    image = imutils.resize(image, width=320)
    sender.send_image('test', image)