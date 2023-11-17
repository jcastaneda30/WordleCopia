import pygame
import sys
import PalabrasPosibles
import random
TriesPosibles = {4:PalabrasPosibles.Letras4,5:PalabrasPosibles.Letras5,6:PalabrasPosibles.Letras6,7:PalabrasPosibles.Letras7,8:PalabrasPosibles.Letras8}
TriePartida = None
pygame.init()

pygame.display.set_caption("Juego Wordle")
icon = pygame.image.load("imagenes/logo.png")
pygame.display.set_icon(icon)

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

#Boton empezar juego de nuevo

rectangulo_nuevo_juego = pygame.Rect(800,550,110,28)
color_boton_nuevo_juego = (81, 157, 176)
iniciar_juego_nuevo = False

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
fuente = pygame.font.SysFont( 'bahnschrift', 19)
pantalla = pygame.display.set_mode(SIZE)
colorPantalla = (218, 245, 245)
pantalla.fill(colorPantalla)
pygame.display.flip()

texto = ''
texto_respuesta = ''

contador = 0
ganadas=0
perdidas=0







def dibujar(palabra,adivinar,columnas):
    global contador,ganadas,perdidas
    ancho_cuadro = (SIZE[0] - (columnas + 1) * 10) // columnas
    conteo_palabras = dict()

    for i in range(len(adivinar)):
        if adivinar[i]==palabra[i]:
            conteo_palabras[adivinar[i]]=0
            continue
        if adivinar[i] not in conteo_palabras:
            conteo_palabras[adivinar[i]]=1
        else:
            conteo_palabras[adivinar[i]]+=1

    for i, letra in enumerate(list(palabra)):

        x = 10 + i * (ancho_cuadro + 10)
        y = 100 + contador * (60 + 10)
        #Logica para cambiar los colores
        if letra == adivinar[i]:
            color = "#6aaa64"
        elif letra in adivinar and conteo_palabras[letra]!=0:
            color = "#c9b458"
            conteo_palabras[letra]-=1
        else:
            color = "#8f9ba1"
        print()
        #Termina lógica
        pygame.draw.rect(pantalla, color, (x, y, ancho_cuadro, 60))
        font = pygame.font.Font(None, 36)
        letra_surface = font.render(letra, True, (0, 0, 0))
        pantalla.blit(letra_surface, (x + ancho_cuadro // 2 - 10, y + 60 // 2 - 10))

    if palabra == adivinar:
        # Boton nuevo juego
        texto_nuevo_juego = fuente.render("Nuevo juego", True, (0, 0, 0))
        pygame.draw.rect(pantalla, color_boton, rectangulo_nuevo_juego)
        pantalla.blit(texto_nuevo_juego, (rectangulo_nuevo_juego.x + 5, rectangulo_nuevo_juego.y + 5))

        ganadas+=1
        #Para que no pueda seguir agregando palabras
        contador=6
        print("gano")

        # Mensaje si gana
        mensaje_gana = fuente.render("Felicidades, adivinó la palabra", True, (0, 0, 0))
        pantalla.blit(mensaje_gana, (rectangulo_nuevo_juego.x-400, rectangulo_nuevo_juego.y+20))

    elif contador>=5:
        # Boton nuevo juego
        texto_nuevo_juego = fuente.render("Nuevo juego", True, (0, 0, 0))
        pygame.draw.rect(pantalla, color_boton, rectangulo_nuevo_juego)
        pantalla.blit(texto_nuevo_juego, (rectangulo_nuevo_juego.x + 5, rectangulo_nuevo_juego.y + 5))

        perdidas+=1
        print("perdio")

        # Mensaje si pierde
        mensaje_pierde = fuente.render(f"Perdiste, la palabra era {adivina}", True, (0, 0, 0))
        pantalla.blit(mensaje_pierde, (rectangulo_nuevo_juego.x-400, rectangulo_nuevo_juego.y+20))
    
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
                active = not active
            else:
                active = False
                
            if rectangulo_empezar_juego.collidepoint(event.pos):
                adivina = escoger_palabra(int(texto))
                contador=0
                iniciar_juego = True
                pantalla.fill(colorPantalla)

                ancho_cuadro = (SIZE[0] - (int(texto) + 1) * 10) // int(texto)
                for fila in range(6):
                    for columna in range(int(texto)):
                        x = 10 + columna * (ancho_cuadro + 10)
                        y = 100 + fila * (60 + 10)
                        pygame.draw.rect(pantalla, "#8f9ba1", (x, y, ancho_cuadro, 60))
                pygame.display.flip()

            if rectangulo_nuevo_juego.collidepoint(event.pos):
                iniciar_juego=False
                enviar_palabra=False
                contador = 0
                texto=""
                texto_respuesta=""
                pantalla.fill(colorPantalla)

            #Usuario selecciona el cuadro de respuesta
            if rectangulo_respuesta.collidepoint(event.pos) and iniciar_juego:
                active_respuesta = not active_respuesta
            else:
                active_respuesta = False
            
            if rectangulo_enviar_palabra.collidepoint(event.pos):
                print("aaaaaaaaaaaaa")
                print(TriePartida.search(texto_respuesta))
                if len(texto_respuesta)==int(texto) and TriePartida.search(texto_respuesta):
                    enviar_palabra = True
                
            # Cambiar color de la caja input
            color_entrada_dificultad = color_active if active else color_inactive
            color_respuesta = color_active_respuesta if active_respuesta else color_inactive_respuesta
            
        if event.type == pygame.KEYDOWN:

            if active:
                
                if event.key == pygame.K_RETURN and 4<=int(texto)<=8:
                    adivina = escoger_palabra(int(texto))
                    contador=0
                    iniciar_juego = True
                    pantalla.fill(colorPantalla)

                    ancho_cuadro = (SIZE[0] - (int(texto) + 1) * 10) // int(texto)
                    for fila in range(6):
                        for columna in range(int(texto)):
                            x = 10 + columna * (ancho_cuadro + 10)
                            y = 100 + fila * (60 + 10)
                            pygame.draw.rect(pantalla, "#8f9ba1", (x, y, ancho_cuadro, 60))
                    pygame.display.flip()

                elif event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif event.unicode in numeros and 4<=int(texto+event.unicode)<=8:
                    texto += event.unicode
            if active_respuesta:
                if event.key == pygame.K_RETURN and len(texto_respuesta)==int(texto) and TriePartida.search(texto_respuesta):
                    enviar_palabra= True
                elif event.key == pygame.K_BACKSPACE:
                    texto_respuesta = texto_respuesta[:-1]
                else:
                    if len(texto_respuesta)<int(texto):
                        texto_respuesta += (event.unicode).lower()
                        print(texto_respuesta)                    

    def escoger_lista(dificultad):
        global TriePartida
        if dificultad==4:
            lista_posible=PalabrasPosibles.Palabras4Letras
            
        elif dificultad==5:
            lista_posible=PalabrasPosibles.Palabras5Letras
            
        elif dificultad==6:
            lista_posible=PalabrasPosibles.Palabras6Letras
            
        elif dificultad==7:
            lista_posible=PalabrasPosibles.Palabras7Letras
            
        elif dificultad==8:
            lista_posible=PalabrasPosibles.Palabras8Letras
            
        return lista_posible

    def escoger_palabra(dificultad):
        global TriePartida
        if dificultad==4:
            adivina=random.choice(PalabrasPosibles.Palabras4Letras)
            TriePartida=TriesPosibles[4]
        elif dificultad==5:
            adivina = random.choice(PalabrasPosibles.Palabras5Letras)
            TriePartida=TriesPosibles[5]
        elif dificultad==6:
            adivina = random.choice(PalabrasPosibles.Palabras6Letras)
            TriePartida=TriesPosibles[6]
        elif dificultad==7:
            adivina = random.choice(PalabrasPosibles.Palabras7Letras)
            TriePartida=TriesPosibles[7]
        elif dificultad==8:
            adivina = random.choice(PalabrasPosibles.Palabras8Letras)
            TriePartida=TriesPosibles[8]
        return adivina

    if enviar_palabra and iniciar_juego and contador<6:
        print(adivina)
        enviar_palabra=False
        dibujar(texto_respuesta,adivina,int(texto))


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

    #GANADAS
    instruccion_ganadas=fuente.render(f"Partidas Ganadas:      {ganadas}", True, (0, 0, 0))
    pantalla.blit(instruccion_ganadas, (100, rectangulo_nuevo_juego.x-250))

    #PERDIDAS
    instruccion_ganadas = fuente.render(f"Partidas Perdidas:      {perdidas}", True, (0, 0, 0))
    pantalla.blit(instruccion_ganadas, (100, rectangulo_nuevo_juego.x - 200))

    pygame.display.flip()