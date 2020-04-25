# run this program to receive and display frames
# stream frames received from the camera to the browser
import cv2
import imutils
from imutils.video import VideoStream
import imagezmq
import socket
# change this to your stream address
path = "rtsp://100.73.79.255:8080//h264_ulaw.sdp"
cap = VideoStream(path)

# change this to your server address
sender = imagezmq.ImageSender(connect_to='tcp://127.0.0.1:5555') 

cam_id = socket.gethostname()
stream = cap.start()

while True:
    frame = stream.read()
    #frame = imutils.resize(frame, width=400)
    sender.send_image(cam_id, frame)
