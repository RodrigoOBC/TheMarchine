import cv2
import os


class recognition:
    def __init__(self,name, path_type):
        self.name = name
        self.path_type = path_type

    def find_type(self):
        paths = [os.path.join(self.path_type, self.name) for self.name in os.listdir(self.path_type)]
        files = [arq for arq in paths if os.path.isfile(arq)]
        for file in files:
            print(file)
            if self.name in file:
                return file
        return 'ola'

    def recoginition_face(self,frame):
        clf = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        frame_face = frame
        gray_face = cv2.cvtColor(frame_face, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray_face)
        for x_face, y_face, w_face, h_face in faces:
            cv2.rectangle(frame_face, (x_face, y_face), (x_face + w_face, y_face + h_face), (255, 0, 0))
        frame_face_with_detect = frame_face
        return frame_face_with_detect