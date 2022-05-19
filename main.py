from PIL import Image
from os import listdir
from os.path import isdir
from numpy import asarray, expand_dims
import numpy as np
import pandas as pd
import os


def load_face(filename):
    img = Image.open(filename)
    img = img.convert("RGB")

    return asarray(img)


def load_faces(directory_src):
    faces = []

    for filename in listdir(directory_src):
        path = directory_src + filename

        faces.append(load_face(path))

    return faces


def load_fotos(directory_src):
    x, y = [], []

    for subidir in listdir(directory_src):

        path = directory_src + subidir + r'/'

        if not isdir(path):
            continue

        faces = load_faces(path)

        labels = [subidir for _ in range(len(faces))]

        x.extend(faces)
        y.extend(labels)

    return asarray(x), asarray(y)


if __name__ == '__main__':
    trainx, trainy = load_fotos('data/faces/')
    print(trainy)
