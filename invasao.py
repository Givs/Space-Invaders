from pygame import *
from jogador import Jogador
from objeto import Objeto
from inimigo import Inimigo
size = (950,700)

pygame.init()
tela = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")
fecha_tela = True
jogador = Jogador('Imagens\\navenova.png')
inimigo = Inimigo('Imagens\\inimigo.png')
imagemfundo = Objeto('Imagens\\fundo.jpg')
jogando = True
relogio = pygame.time.Clock()

while fecha_tela:
    relogio.tick(50)
    while fecha_tela:
        relogio.tick(50)  # velocidade que a bala vai
        balaJogador.trajetoria()
        balaInimigo.trajetoria()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fecha_tela = False
            if event.type == pygame.KEYDOWN:  # pega alguem evento do teclado
                if event.key == pygame.K_LEFT:
                    jogador.mover('esquerda')

                elif event.key == pygame.K_RIGHT:
                    jogador.mover('direita')

                elif event.key == pygame.K_SPACE:
                    rect = jogador.get_rect()
                    x,y = rect.center
                    jogador.disparar(x,y)

        tela.blit(imagemfundo, (0, 0))
        jogador.colocar(tela)  # chama a funçao pra botar as coisas na tela
        inimigo.colocar(tela)

        if len(jogador.get_diparos()) > 0:
            for x in jogador.get_diparos():
                x.colocar(tela)
                x.trajetoria()
        if len(inimigo.listaDisparo) > 0:
            for y in inimigo.listaDisparo:
                y.colocar(playsurface)
                y.trajetoria()
        if len(inimigo2.listaDisparo) > 0:
            for w in inimigo2.listaDisparo:
                w.colocar(playsurface)
                w.trajetoria()

        pygame.display.update()

    pygame.quit()

invasao()


