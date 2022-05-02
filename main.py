import os
import cv2
from utils.facial_recognition import recognition
from utils.imageData import WebCam


if __name__ == '__main__':
    WebCam1 = WebCam()
    frame = WebCam1.capture_webcam()
    cv2path = os.path.dirname(cv2.__file__)
    RE_FACE = recognition('haarcascade_frontalface_alt2.xml', fr'{cv2path}\data')
    frame_with_detect = RE_FACE.recoginition_face(frame)
    WebCam1.save_frame(frame_with_detect)
