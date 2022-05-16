from os import path, listdir
import cv2
from PIL import Image
from numpy import asarray
import numpy as np
from mtcnn import MTCNN


class Image_father:
    def __init__(self):
        pass

    def flip_image(self, image):
        img = image.transpose(Image.FLIP_LEFT_RIGHT)
        return img

    def rotate_90(self, image):
        img = image.transpose(Image.ROTATE_90)
        return img

    def extrair_face(self, arquivo, size=(160, 160)):
        detector = MTCNN()
        img = Image.open(arquivo)
        img_RGB = img.convert('RGB')
        img_array = asarray(img_RGB)
        results = detector.detect_faces(img_array)
        x1, y1, w1, h1 = results[0]['box']
        x2, y2 = x1 + w1, y1 + h1
        face = img_array[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(size)
        return image

    def save_fotos(self, file_path, path_target):
        for filename in listdir(file_path):
            src_path = file_path + filename
            tgt_path = path_target + filename
            flip_path = f'{path_target}flip-{filename}'
            rotate_path = f'{path_target}rotate-{filename}'

            try:
                face = self.extrair_face(src_path)
                flip_face = self.flip_image(face)
                rotate_face = self.rotate_90(face)
                face.save(tgt_path, "JPEG", quality=100, optimize=True, progressive=True)
                print(f'save   {tgt_path}')
                flip_face.save(flip_path, "JPEG", quality=100, optimize=True, progressive=True)
                print(f'save   {flip_path}')
                rotate_face.save(rotate_path, "JPEG", quality=100, optimize=True, progressive=True)
                print(f'save   {rotate_path}')
                print('----------------------------//--------------------------------------------')
            except:
                print(f'Erro na imagem {src_path}')


class WebCam(Image_father):
    def __init__(self, video=0):
        self.cap = None
        self.video = video
        self.FILE_SAVE_PATH = 'data/fotos_webcam/'

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

    def save_frame(self, frame=''):
        frame = self.capture_webcam()
        cv2.imwrite(r"data/fotos_webcam/teste.jpg", frame)
        print('teste')

    def save_fotos(self, file_path='data/fotos_webcam/', path_target=''):
        pass


class Photo(Image_father):
    def __init__(self, diretorio_scr, diretorio_tgt):
        super().__init__()
        self.diretorio_scr = diretorio_scr
        self.diretorio_tgt = diretorio_tgt

    def load_dir(self):
        for subdir in listdir(self.diretorio_scr):
            file_path = self.diretorio_scr + subdir + '/'
            path_target = self.diretorio_tgt + subdir + '/'

            if not path.isdir(file_path):
                continue
            self.save_fotos(file_path, path_target)
