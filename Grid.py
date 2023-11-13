import pygame, sys
pygame.init()
window=pygame.display.set_mode((500, 500))  # Cambia el tamaño de la ventana a 500x500
font=pygame.font.SysFont('arial', 40)
text=font.render('@asdf', True, (0, 0, 0))
rect=text.get_rect()
rect.x = 200  # Cambia la posición x del texto a 200
rect.y = 200  # Cambia la posición y del texto a 200
window.fill((255, 255, 255))
window.blit(text, rect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()