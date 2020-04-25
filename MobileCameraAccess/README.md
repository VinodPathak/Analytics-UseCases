## Requirements


1. create conda environment
2. conda create -n avatar python==3.7.6
3. conda activate avatar
4. pip install following packages:
- opencv-python
- imutils
- socket
- imagezmq
5. create file(capture, convert and send), capture from rtsp server(mobile phone/ip camera) and send frame to tcp server
6. create file(capture and show), capture from above and send to opencv imshow
