from nave import Nave

class Jogador(Nave):
    def __init__(self,imagem):
        super().__init__(imagem)

    def mover(self,direcao):
        if direcao == "direita":
            self.__rect.right += self.__velocidade
            if self.__rect.right > 950:
                self.__rect.right = 950
        if direcao == "esquerda":
             self.__rect.left -= self.__velocidade
             if self.__rect.left <= 0:
                self.__rect.left = 0