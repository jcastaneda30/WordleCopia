abecedario_minusculas = "abcdefghijklmnopqrstuvwxyz"
# Abre el archivo de entrada en modo lectura
with open('top-10000-spanish-words.txt', 'r') as entrada:
    # Lee cada línea del archivo de entrada
    lineas = [palabra.strip() for palabra in entrada.readlines()]

# Procesa las líneas si es necesario
# Aquí puedes realizar cualquier manipulación o análisis de las líneas leídas

# Nombre del archivo de salida
with open('Longitud8.txt', 'w') as salida:
    # Escribe las líneas procesadas en el archivo de salida
    for linea in lineas:
        a=True
        print(linea)
        if len(linea)==8:
            for letra in linea:
                if letra not in abecedario_minusculas:
                    a=False
                    break
            if a: salida.write(linea+'\n')
