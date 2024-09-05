import pygame
import random

pygame.init()

LARGURA_JANELA = 500
ALTURA_JANELA = 800
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
PASSARO_AZUL = (0, 0, 255)

tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Passarinho")

class Passaro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 0
        self.altura_pulo = 0
        self.TAM_PASSARO = (50, 50)

    def atualizar(self):
        self.velocidade += 0.5
        if self.altura_pulo < 10:
            self.altura_pulo += 2
        else:
            self.altura_pulo = 10
        if self.y > ALTURA_JANELA - self.TAM_PASSARO[1]:
            self.y = ALTURA_JANELA - self.TAM_PASSARO[1]
        self.y += self.velocidade
        self.velocidade -= 0.5
        if self.velocidade < 0:
            self.velocidade = 0
        self.altura_pulo -= 1

    def pular(self):
        self.velocidade = -10

    def desenhar(self, tela):
        pygame.draw.rect(tela, PASSARO_AZUL, (self.x, self.y, self.TAM_PASSARO[0], self.TAM_PASSARO[1]))


class Cano:
    def __init__(self, x, y, comp):
        self.x = x
        self.y = y
        self.comp = comp
        self.velocidade = -2
        self.TAM_CANO = (52, 400)

    def atualizar(self):
        self.x += self.velocidade

    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, (self.x, self.y, self.comp, self.TAM_CANO[1]))


class CanoInvertido:
    def __init__(self, x, y, comp):
        self.x = x
        self.y = y
        self.comp = comp
        self.velocidade = -2
        self.TAM_CANO = (52, 400)

    def atualizar(self):
        self.x += self.velocidade

    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, (self.x, self.y + self.TAM_CANO[1], self.comp, self.TAM_CANO[1]))


def desenhar_tela_jogando(tela, canos, passaro, pontuacao):
    tela.fill(PRETO)
    for cano in canos:
        pygame.draw.rect(tela, BRANCO, cano)
    pygame.draw.rect(tela, BRANCO, passaro)
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render("Pontuação: " + str(pontuacao), True, BRANCO)
    tela.blit(texto, (10, 10))


def main():
    passaro = Passaro(LARGURA_JANELA // 2, ALTURA_JANELA // 2)
    canos = []
    ultimo_cano = pygame.time.get_ticks()
    pontuacao = 0

    relogio = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    passaro.pular()

        tela.fill(PRETO)
        if pygame.time.get_ticks() - ultimo_cano > 3000 and len(canos) < 5:
            cano_x = LARGURA_JANELA
            cano_altura = random.randint(50, ALTURA_JANELA - 250)
            cano1 = Cano(cano_x, ALTURA_JANELA - cano_altura - 120, 52)
            cano2 = CanoInvertido(cano_x, 0, 52)
            canos.append(cano1)
            canos.append(cano2)
            ultimo_cano = pygame.time.get_ticks()

        for cano in canos:
            cano.atualizar()
            if cano.x < passaro.x + passaro.TAM_PASSARO[0] and cano.x + cano.comp > passaro.x:
                if cano.y < passaro.y + passaro.TAM_PASSARO[1] and cano.y + cano.TAM_CANO[1] > passaro.y:
                    pass
                if cano.y < passaro.y + passaro.TAM_PASSARO[1] and cano.y + cano.TAM_CANO[1] > passaro.y:
                    pass
                if cano.y < passaro.y + passaro.TAM_PASSARO[1] and cano.y + cano.TAM_CANO[1] > passaro.y:
                    pass

        if pygame.time.get_ticks() - ultimo_cano > 3000 and len(canos) < 5:
            cano_x = LARGURA_JANELA
            cano_altura = random.randint(50, ALTURA_JANELA - 250)
            cano1 = Cano(cano_x, ALTURA_JANELA - cano_altura - 120, 52)
            cano2 = CanoInvertido(cano_x, 0, 52)
            canos.append(cano1)
            canos.append(cano2)
            ultimo_cano = pygame.time.get_ticks()

        if passaro.y + passaro.TAM_PASSARO[1] >= ALTURA_JANELA:
            pass

        passaro.atualizar()

        canos_passados = [cano for cano in canos if cano.x + cano.comp < passaro.x]
        pontuacao += len(canos_passados)

        for cano in canos_passados:
            canos.remove(cano)

        for cano in canos:
            if cano.x < passaro.x and cano.x + cano.comp > passaro.x:
                if cano.y < passaro.y + passaro.TAM_PASSARO[1] and cano.y + cano.TAM_CANO[1] > passaro.y:
                    pass

        passaro.desenhar(tela)

        for cano in canos:
            cano.desenhar(tela)

        desenhar_tela_jogando(tela, canos, passaro, pontuacao)

        pygame.display.update()
        relogio.tick(30)


main()