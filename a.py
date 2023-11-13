a=[5.9,
7.6,
8.2,
7.8,
7.2,
6.8,
8.7,
7.7,
7.3,
6.5,
7.8,
11.6,
6.3,
7.0,
9.7,
11.3,
8.1,
6.3,
7.4,
11.8,
6.8,
7.9,
7.7,
10.7,
7.0,
9.0,
9.7]
def media(lista:list)->int:
    suma =0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma/len(lista)
def IC(lista:list,t:int)->tuple:
    promedio = media(lista)
    return (promedio-t,promedio+t)
print(media(a))
print(IC(a,2.06))