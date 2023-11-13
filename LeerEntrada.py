import pygame
import sys

pygame.init()

# Crear la pantalla
display = pygame.display.set_mode((300, 300))
letra_presionada = ''
# Crear una fuente para mostrar la tecla presionada
font = pygame.font.Font(None, 36)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Verificar si es una tecla alfanumérica
            if event.unicode.isalpha():
                letra_presionada = event.unicode
                print(f"Letra presionada: {letra_presionada}")

    # Limpiar la pantalla
    display.fill((255, 255, 255))

    # Mostrar la tecla presionada en la pantalla
    texto = font.render(f"Letra: {letra_presionada}", True, (0, 0, 0))
    display.blit(texto, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()
