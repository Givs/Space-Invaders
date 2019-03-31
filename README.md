import pygame
from random import randint
import sys
import os
import time

#color = pygame.Color(255,255,255,255)
width = 950
height = 700
size = (width, height)

class Inimigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemInimigo = pygame.image.load('inimigo.png')
        self.ImagemInimigo = pygame.image.load('inimigo.png')
        self.rect = self.ImagemInimigo.get_rect()


        self.listaDisparo = []
        self.velocidade = 20
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        pass
        #self.rect.top = self.rect.top - self.velocidadeBala

    def colocar(self,superficie):
        superficie.blit(self.ImagemInimigo, self.rect)

    def disparar(self,x,y):
        balaInimigo = BalaInimigo(x,y)
        self.listaDisparo.append(balaInimigo)

class BalaInimigo (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBalaInimigo = pygame.image.load('balaouro.png')

        self.rect = self.ImagemBalaInimigo.get_rect()
        self.velocidadeBala = 5
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top = self.rect.top + self.velocidadeBala

    def colocar(self,superficie):
        superficie.blit(self.ImagemBalaInimigo, self.rect)

class Bala(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('balaprata.png')

        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 5
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala

    def colocar(self,superficie):
        superficie.blit(self.ImagemBala, self.rect)

class nave_espacial(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load('navenova.png')

        self.rect = self.ImagemNave.get_rect() #cria um retangulo na imagem pra trabalhar colisões
        self.rect.centerx = width / 2   #local que a nave vai iniciar
        self.rect.centery = height - 50

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()
    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 950:
                self.rect.right = 950

    def disparar(self,x,y):
        minhabala = Bala(x,y)
        self.listaDisparo.append(minhabala)

    def colocar(self,superfice):
        superfice.blit(self.ImagemNave, self.rect)  #coloca na tela a nave(.blit)


#função principal
def invasao():
    pygame.init()
    playsurface = pygame.display.set_mode(size)  #tamanho da tela
    pygame.display.set_caption("Space Invaders")  #titulo na janela
    relogio = pygame.time.Clock()

    fecha_tela = True
    jogador = nave_espacial()
    imagemfundo = pygame.image.load('fundo.jpg')
    jogando = True
    inimigo = Inimigo(100,50)
    balaJogador = Bala(width / 2, height - 60)
    balaInimigo = BalaInimigo(width /2, height - 60)
    audio_tiro = pygame.mixer.Sound('tironave2.1.ogg')
    while fecha_tela:
        relogio.tick(50)               #velocidade que a bala vai
        balaJogador.trajetoria()
        balaInimigo.trajetoria()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fecha_tela = False
            if event.type == pygame.KEYDOWN:       #pega alguem evento do teclado
                if event.key == pygame.K_LEFT:
                    jogador.movimentoEsquerda()

                elif event.key == pygame.K_0:
                    x,y = inimigo.rect.center
                    inimigo.disparar(x,y)

                elif event.key == pygame.K_RIGHT:
                        jogador.movimentoDireita()

                elif event.key == pygame.K_SPACE:
                    x,y = jogador.rect.center
                    audio_tiro.play()
                    jogador.disparar(x,y)

        playsurface.blit(imagemfundo, (0,0))
        jogador.colocar(playsurface)   #chama a funçao pra botar as coisas na tela
        inimigo.colocar(playsurface)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(playsurface)
                x.trajetoria()
        if len(inimigo.listaDisparo) > 0:
            for y in inimigo.listaDisparo:
                y.colocar(playsurface)
                y.trajetoria()
        pygame.display.update()


    pygame.quit()

invasao()
