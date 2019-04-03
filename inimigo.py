from nave import Nave
from pygame import mixer


class Inimigo(Nave):
    def __init__(self, imagem):
        super().__init__(imagem)
        self.__efeito = mixer.Sound("audios\\colisao.ogg")

    def destruir(self):
        self.__efeito.play()

