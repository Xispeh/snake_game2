
import pygame
from pygame.locals import *
from sys import exit
from random import randint
# IMPORTE SEMPRE ESSAS BIBLIOTECAS PARA CRIAR O GAME:
pygame.init()
# função importante para iniciar o pygame.
largura=800
altura=600
# DEFINA LARGURA E ALTURA largura=x altura=y
x=largura/2-20
y=altura/2-20
xx=randint(20,780)
yy=randint(20,580)
#DEFINIR ELAS PARA CONTROLAR O MOVIMENTO DE UM OBJETO
fonte= pygame.font.SysFont('arial',40, False, False)
#criação de uma VARIAVEL FONTE,estilo da letra, tamanho, negrito, italico
#pra achar outras fontes, pesquisa no console: pygame.font.get_fonts()
pontos=0
tentativa=0
#sistema de pontuação
tela=pygame.display.set_mode((largura, altura))
#FUNÇÃO PARA CRIAR O DISPLAY
pygame.display.set_caption("Xispeh game")
#FUNÇÃO PARA CRIAR A LEGENDA DO TÍTULO DA JANELA
clock=pygame.time.Clock()
#cria um relogio
pygame.mixer.music.set_volume(0.1)
#abaixar o volume da musica, valor entre 0 e 1, sendo que 0 vc tira o som
music=pygame.mixer.music.load('music.mp3')
#a musica de fundo sempre tem que ser em .mp3
pygame.mixer.music.play(-1)
#o efeito -1, faz com que a musica se repita pra sempre
colisao=pygame.mixer.Sound("coin.wav")
#efeito sonoros do game, sempre tem que ser em .wav
gameover=pygame.mixer.Sound("game_over.wav")
lista_cobra = []
velocidade=10
quadrado_cobra=20
#velocidade que a cobra anda
x_controle=velocidade
#velocidade da cobra controlada
y_controle=0
#velocidade da cobra controlada
comprimento_inicial = 5
#com quantos quadrados a cobra vai começar
morreu = False
#funcao que define a morte da cobra, ela encostar nela mesma
def aumenta_cobra(lista_cobra):
    #funcao que vai aumentar a cobra
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], quadrado_cobra, quadrado_cobra))
def reiniciar_jogo():
    global pontos, comprimento_inicial, x, y, lista_cobra, lista_cabeca, xx, yy, morreu, tentativa, message, tent, velocidade
    pontos = 0
    velocidade = 10
    comprimento_inicial = 5
    x = largura/2-20
    y = largura/2-20
    lista_cobra = []
    lista_cabeca = []
    xx = randint(20, 780)
    yy = randint(20, 580)
    morreu = False
    tentativa = tentativa + 1
while True:
    clock.tick(30)
    #diz em quantos ticks em um segundo o jogo vai rodar
    tela.fill((90,150,17))
    #COMPLETA A TELA TODO O DISPLAY COM A COR PRETA
    for event in pygame.event.get():
        if event.type == QUIT:
            #registra o evento de clicar o X da janela.
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            #registra o pressionamento de uma tecla
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                #registra a tecla A quando pressionada
                    x_controle=-velocidade
                    y_controle=0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
                # registra a tecla D quando pressionada
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle= -velocidade
                    x_controle=0
                # registra a tecla W quando pressionada
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle= velocidade
                    x_controle=0
    x= x +x_controle
    y= y +y_controle
                # registra a tecla S quando pressionada
            # registra a tela sempre pressionada
    # UM WHILE TRUE QUE MANTEM O JOGO SEMPRE EM ATUALIZAÇÃO

    snake=pygame.draw.rect(tela, (0, 255, 0), (x, y, quadrado_cobra, quadrado_cobra))
    #todo o retangulo dentro uma variavel
    apple=pygame.draw.rect(tela, (255, 0, 0), (xx, yy, 20, 20))
    #todo o retangulo dentro uma variavel
    if snake.colliderect(apple):
        #funcao que identifica a colisao de uma variavel com a outra
        xx=randint(20,780)
        yy=randint(20,580)
        # nao pode ser maior que o valor do objeto, pra nao ser invadir a tela
        pontos+=1
        colisao.play()
        #rodar o efeito sonoro da colisao
        comprimento_inicial+=1
        velocidade+=0.5


    lista_cabeca=[]
    lista_cabeca.append(x)
    lista_cabeca.append(y)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) >1:
        #funcao que determina que a cobra entrou nela mesma.
        morreu = True
        gameover.play()
        fonte2 = pygame.font.SysFont('arial', 20, False, False)
        mensagemm= 'PERDEU OTARIO! - Pressione R'
        texto=fonte2.render(mensagemm, False, (255, 255, 255))
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    #funcao de fechar o jogo
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto,((largura/2)-120, (altura/2)-50))
            pygame.display.update()

    aumenta_cobra(lista_cobra)
    #funcao em loop que vai aumentar a cobra
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
        #isso daqui diz que o tamanho da cobra for maior que o inicial, vai remover
    chat=f"Score: {pontos}"
    chatt=f"Tentativa: {tentativa}"
    #definicao da pontuação e tentativas a ser exibido
    message=fonte.render(chat, True, (0, 0, 0))
    tent=fonte.render(chatt, True, (0, 0, 0))
    #formatação do texto na tela. objeto, cerrilhamento, (R, G, B)
    tela.blit(message, (largura-150, 10))
    tela.blit(tent, (20,10))
    #aparecer o texto na tela.
    if x > largura:
        morreu = True
        gameover.play()
        fonte2 = pygame.font.SysFont('arial', 20, False, False)
        mensagemm = 'PERDEU OTARIO! - Pressione R'
        texto = fonte2.render(mensagemm, False, (255, 255, 255))
        while morreu:
            tela.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    # funcao de fechar o jogo
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto, ((largura / 2) - 120, (altura / 2) - 50))
            pygame.display.update()
    if x < 0:
        morreu = True
        gameover.play()
        fonte2 = pygame.font.SysFont('arial', 20, False, False)
        mensagemm = 'PERDEU OTARIO! - Pressione R'
        texto = fonte2.render(mensagemm, False, (255, 255, 255))
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    # funcao de fechar o jogo
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto, ((largura / 2) - 120, (altura / 2) - 50))
            pygame.display.update()
    if y > altura:
        morreu = True
        gameover.play()
        fonte2 = pygame.font.SysFont('arial', 20, False, False)
        mensagemm = 'PERDEU OTARIO! - Pressione R'
        texto = fonte2.render(mensagemm, False, (255, 255, 255))
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    # funcao de fechar o jogo
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto, ((largura / 2) - 120, (altura / 2) - 50))
            pygame.display.update()
    if y < 0:
        morreu = True
        gameover.play()
        fonte2 = pygame.font.SysFont('arial', 20, False, False)
        mensagemm = 'PERDEU OTARIO! - Pressione R'
        texto = fonte2.render(mensagemm, False, (255, 255, 255))
        #criação do texto perdeu otario
        while morreu:
            tela.fill((0, 0, 0))
            #deixa a tela toda preta
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    # funcao de fechar o jogo
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto, ((largura / 2) - 120, (altura / 2) - 50))
            #exibição do texto game over
            pygame.display.update()
    pygame.display.update()
    #atualiza sempre o display