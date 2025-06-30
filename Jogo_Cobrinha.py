import pygame
import time
time.sleep(2)
import random

# Inicializar o pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')


imagem_fundo = pygame.image.load(r'Assets/images/Fundo.png').convert_alpha()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

imagem_game_over = pygame.image.load(r'Assets/images/fundoGameOver.png').convert_alpha()
imagem_game_over = pygame.transform.scale(imagem_game_over, (largura, altura))


# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Configurações da cobra do tamanho da cobra e da velocidade
tamanho_celula = 10
velocidade = 15

fonte = pygame.font.SysFont("poppins", 25)

#Blit: No Pygame, o método `.blit()` é usado para desenhar uma superfície (como uma imagem ou texto) em outra superfície, geralmente a tela principal do jogo. Ele "copia" o conteúdo de uma superfície para outra em uma posição específica. No seu código, o método `.blit()` é usado na função `mensagem` para exibir texto na tela: Aqui, o texto renderizado pela fonte (`fonte.render`) é desenhado na superfície `tela` na posição especificada por `[largura / 6, altura / 3]`. Isso permite exibir mensagens, como "Você perdeu!" no jogo.

##Imagens 
imagem_maca = pygame.image.load(r'Assets/images/maca.png').convert_alpha()

# O método `convert_alpha()` é usado para otimizar a imagem para renderização

imagem_maca = pygame.transform.scale(imagem_maca, (tamanho_celula, tamanho_celula))

# Função para exibir mensagens na tela
def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo():
    fim_jogo = False
    game_over = False

    x1 = largura / 2
    y1 = altura / 2

    x1_mudanca = 0
    y1_mudanca = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_celula) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_celula) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not fim_jogo:

        while game_over:
            tela.blit(imagem_game_over, (0, 0))
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_celula
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_celula
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_celula
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_celula
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_over = True

        x1 += x1_mudanca
        y1 += y1_mudanca

        tela.blit(imagem_fundo, (0, 0))
        
        tela.blit(imagem_maca, (comida_x, comida_y))
        corpo_cobra.append([x1, y1])
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for bloco in corpo_cobra[:-1]:
            if bloco == [x1, y1]:
                game_over = True

        for bloco in corpo_cobra:
            pygame.draw.rect(tela, preto, [bloco[0], bloco[1], tamanho_celula, tamanho_celula])

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_celula) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_celula) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()