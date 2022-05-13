from os import path, listdir
import cv2
from PIL import Image
from numpy import asarray, array
from mtcnn import MTCNN


def extrair_face(arquivo, size=(160, 160)):
    detector = MTCNN()
    img = Image.open(arquivo)
    img_rgb = img.convert('RGB')
    img_array = asarray(img_rgb)
    results = detector.detect_faces(img_array)
    x1, y1, w1, h1 = results[0]['box']
    x2, y2 = x1 + w1, y1 + h1
    face = array[x1:y2, y1:y2]
    image = Image.fromarray(face)
    image = image.resize(size)
    return image


def load_dir(diretorio_scr, diretorio_tgt):
    for subdir in listdir(diretorio_scr):
        file_path = diretorio_scr + subdir + '\\'
        path_target = diretorio_tgt + subdir + '\\'

        if not path.isdir(file_path):
            continue
        load_fotos(file_path, path_target)


def load_fotos(diretorio_scr, diretorio_tgt):
    print(diretorio_scr)
    print(diretorio_tgt)


if __name__ == '__main__':
    load_dir(r'data/fotos/Sr_Rodrigo/',r'data/faces/Sr_Rodrigo/')
