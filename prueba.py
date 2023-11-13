import pygame
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color = (218, 245, 245)
screen.fill(color)
pygame.display.flip()
run = True
while run:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            run = False
pygame.quit()
