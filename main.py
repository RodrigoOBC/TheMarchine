from utils.imageData import Photo


if __name__ == '__main__':
    Foto = Photo(r'data/fotos/', r'data/faces/')
    Foto.load_dir()
