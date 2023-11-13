import pygame
import sys

pygame.init()
numeros = ['4','5','6','7','8']
# Escribir dificultad
rectangulo_user_input = pygame.Rect(390, 40, 140, 28)
color_inactive = (61, 71, 105)
color_active = (54, 89, 201)
color_entrada_dificultad = color_inactive
active = False

#Boton comenzar
rectangulo_empezar_juego = pygame.Rect(630, 40, 85, 28)
color_boton = (81, 157, 176)
iniciar_juego = False

#Escribir palabra
rectangulo_respuesta = pygame.Rect(390, 630, 140, 28)
color_inactive_respuesta = (61, 71, 105)
color_active_respuesta = (54, 89, 201)
color_respuesta = color_inactive
active_respuesta = False

#Boton enviar palabra
rectangulo_enviar_palabra = pygame.Rect(630, 630, 100, 28)
color_boton_enviar_palabra = (81, 157, 176)
enviar_palabra = False

# Pantalla base
SIZE = (980, 720)
fuente = pygame.font.SysFont(None, 25)
pantalla = pygame.display.set_mode(SIZE)
colorPantalla = (218, 245, 245)
pantalla.fill(colorPantalla)
pygame.display.flip()

texto = ''
texto_respuesta = ''

contador = 0


def dibujar(palabra,adivinar,columnas):
    global contador
    ancho_cuadro = (SIZE[0] - (columnas + 1) * 10) // columnas
    for i, letra in enumerate(list(palabra)):
        x = 10 + i * (ancho_cuadro + 10)
        y = 100 + contador * (60 + 10)
        #Logica para cambiar los colores
        if letra == adivinar[i]:
            color = "#a2f285"
        elif letra in adivinar:
            color = "#d985f2"
        else:
            color = "#8f9ba1"
        #Termina lógica
        pygame.draw.rect(pantalla, color, (x, y, ancho_cuadro, 60))
        font = pygame.font.Font(None, 36)
        letra_surface = font.render(letra, True, (0, 0, 0))
        pantalla.blit(letra_surface, (x + ancho_cuadro // 2 - 10, y + 60 // 2 - 10))

    if palabra == adivinar:
        pass #Aquí que pasa si gana
    
    contador += 1
    pygame.display.update()

pantalla.fill(colorPantalla)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Usuario selecciona la dificultad
            if rectangulo_user_input.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
                
            if rectangulo_empezar_juego.collidepoint(event.pos):
                iniciar_juego = True
                pantalla.fill(colorPantalla)


            #Usuario selecciona el cuadro de respuesta
            if rectangulo_respuesta.collidepoint(event.pos):
                # Toggle the active variable.
                active_respuesta = not active_respuesta
            else:
                active_respuesta = False
            
            if rectangulo_enviar_palabra.collidepoint(event.pos):
                enviar_palabra = True
                
            # Change the current color of the input box.
            color_entrada_dificultad = color_active if active else color_inactive
            color_respuesta = color_active_respuesta if active_respuesta else color_inactive_respuesta
            
            
            
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(texto)
                    texto = ''
                elif event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif event.unicode in numeros and 4<=int(texto+event.unicode)<=8:
                    texto += event.unicode
            if active_respuesta:
                if event.key == pygame.K_RETURN:
                    texto_respuesta = ''
                elif event.key == pygame.K_BACKSPACE:
                    texto_respuesta = texto_respuesta[:-1]
                else:
                    texto_respuesta += (event.unicode).lower()
                    print(texto_respuesta)

    if enviar_palabra:
        enviar_palabra=False
        dibujar(texto_respuesta,"vicioooo",int(texto))
    
    
    
    # Intrucciones
    instruccion = fuente.render("Da click y escribe la dificultad de 4 a 8", True, (0, 0, 0))
    pantalla.blit(instruccion, (350, rectangulo_user_input.y + 35))
    
    # Seleccionar dificultad
    txt_surface = fuente.render(texto, True, (0, 0, 0))
    width = max(200, txt_surface.get_width() + 10)
    rectangulo_user_input.w = width
    pygame.draw.rect(pantalla, color_entrada_dificultad, rectangulo_user_input)
    pantalla.blit(txt_surface, (rectangulo_user_input.x + 90, rectangulo_user_input.y + 5))
    
    #Boton de inicio
    textoComenzar = fuente.render("Empezar", True, (0, 0, 0))
    pygame.draw.rect(pantalla, color_boton, rectangulo_empezar_juego)
    pantalla.blit(textoComenzar, (rectangulo_empezar_juego.x + 5, rectangulo_empezar_juego.y + 5))
    
    
    #Escribir palabra juego
    txt_respuesta = fuente.render(texto_respuesta, True, (0, 0, 0))
    width_respuesta = max(200, txt_respuesta.get_width() + 10)
    rectangulo_respuesta.w = width
    pygame.draw.rect(pantalla, color_respuesta, rectangulo_respuesta)
    pantalla.blit(txt_respuesta, (rectangulo_respuesta.x + 5, rectangulo_respuesta.y + 5))
    
    #Boton de enviar palabra
    texto_enviar = fuente.render("Comprobar", True, (0, 0, 0))
    pygame.draw.rect(pantalla, color_boton_enviar_palabra, rectangulo_enviar_palabra)
    pantalla.blit(texto_enviar, (rectangulo_enviar_palabra.x + 5, rectangulo_enviar_palabra.y + 5))
    
    # Intrucciones
    instruccion_respuesta = fuente.render("Escribe aqui la palabra que creas que pueda ser", True, (0, 0, 0))
    pantalla.blit(instruccion_respuesta, (350, rectangulo_respuesta.y + 35))

    pygame.display.flip()