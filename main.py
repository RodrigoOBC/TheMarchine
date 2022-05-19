from utils.imageData import Photo,WebCam


if __name__ == '__main__':
    Foto = WebCam()
    filename = 'foto_teste'
    Foto.save_frame('data/faces/fotos_webcam/',filename)
