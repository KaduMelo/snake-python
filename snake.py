import pygame

azul = (50,100, 213)
laranja = (205, 102, 0)

dimensoes = (600, 600)

### VALROES INICIAIS ###
x = 300
y = 300

d = 20

tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Snake')

tela.fill(azul)

clock = pygame.time.Clock()

def desenha_cobra():
    pygame.draw.rect(tela, laranja, [x, y , d, d])

while True:
    pygame.display.update()
    desenha_cobra()
    # mover_cobra()
    clock.tick(1)