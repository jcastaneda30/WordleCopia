import pygame
import sys
import random

# Inicializar la librería
pygame.init()

# Tamaño de la ventana
SIZE = (700, 600)
SCREEN = pygame.display.set_mode(SIZE)

# Nombre ventana e icono
pygame.display.set_caption("Juego Wordle")
ICON = pygame.image.load("imagenes/logo.png")
pygame.display.set_icon(ICON)


# Palabra a adivinar 
adivinar = random.choice(["hola"])

# Colores
GREEN = "#a2f285"
PURPLE = "#d985f2"
GREY = "#8f9ba1"
BASE = "#dae0e3"

# Color pantalla
SCREEN.fill("white")

# Número de filas y columnas
filas = 6
columnas = len(adivinar)

# Espaciado entre cuadros
espaciado_x = 10
espaciado_y = 10

# Ancho de cada cuadro
ancho_cuadro = (SIZE[0] - (columnas + 1) * espaciado_x) // columnas

# Alto de cada cuadro
alto_cuadro = 60

pygame.display.update()

contador = 0

def dibujar(palabra):
    global contador

    for i, letra in enumerate(list(palabra)):
        x = espaciado_x + i * (ancho_cuadro + espaciado_x)
        y = 100 + contador * (alto_cuadro + espaciado_y)
        #Logica para cambiar los colores
        if letra == adivinar[i]:
            color = GREEN
        elif letra in adivinar:
            color == PURPLE
        else:
            color = GREY
        #Termina lógica
        pygame.draw.rect(SCREEN, color, (x, y, ancho_cuadro, alto_cuadro))
        font = pygame.font.Font(None, 36)
        letra_surface = font.render(letra, True, (0, 0, 0))
        SCREEN.blit(letra_surface, (x + ancho_cuadro // 2 - 10, y + alto_cuadro // 2 - 10))

    if palabra == adivinar:
        pass #Aquí que pasa si gana
    
    contador += 1
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: #El evento de presionar el botón
            palabra_ingresada = '' #El texto que se extrae del cuadrito
            if palabra_ingresada.lower() in [""]:
                dibujar(palabra_ingresada)