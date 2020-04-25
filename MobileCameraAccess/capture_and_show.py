# run this program to receive and display frames
# stream frames received from the camera to the browser
import cv2
import imagezmq

	
# When there is a request from the web browser, create a subscriber
image_hub = imagezmq.ImageHub(open_port='tcp://127.0.0.1:5555')
while True:  # show streamed images
    rpi_name, image = image_hub.recv_image()
    cv2.imshow(rpi_name, image) # 1 window for each RPi
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')
