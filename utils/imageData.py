import cv2
import os


class WebCam:
    def __init__(self, video=0):
        self.cap = None
        self.video = video

    def set_cap(self):
        self.cap = cv2.VideoCapture(self.video)

    def capture_webcam(self):
        self.set_cap()
        ret, frame = self.cap.read()
        cv2.imshow('webcam video', frame)
        self.cap.release()
        cv2.waitKey(1)
        self.cap.release()
        self.close_webcam()
        return frame

    def close_webcam(self):
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    def save_frame(self, frame):
        cv2.imwrite(r"data/fotos_webcam/teste.jpg", frame)
        print('teste')