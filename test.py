from CameraClass import Camera
import cv2

while(1):
    cam = Camera(camAddress = 0)
    cam.start()
    while(1):
        # cam.setDaemon(True)
        fr = cam.getFrame()
        cv2.imshow("fr", fr)
        cv2.waitKey(10)

    cam.closeCam()
