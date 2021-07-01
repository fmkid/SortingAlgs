def sort(lista):
    pasos = 0
    long = len(lista)
    
    factor = 2
    a = 2.1
    b = 3
    if long > 14:
        while factor * int(a * factor + b) <= long:
            factor += 1
    factor -= 1
    distancia = long//factor
    
    while long > 1:
        for i in range(0, distancia):
            for j in range(i, long - distancia, distancia):
                next = j + distancia
                if lista[j] > lista[next]:
                    lista[j], lista[next] = lista[next], lista[j]
                pasos += 1
        distancia -= 1
        if not distancia:
            break
    return (lista, pasos, factor)              
    

from random import shuffle#, randrange
'''
cant = 50

valores = [i for i in range(cant)]
#valores = [i for i in range(cant,0,-1)]
#valores = [1 for i in range(cant)]
#valores = [randrange(0,cant) for i in range(cant)]
#valores = [0 for i in range(cant)] + [1 for j in range(cant)]

shuffle(valores)
copia = valores[:]

print("Lista original:\n", valores)
resultado = sort(valores)
print("\nLista ordenada:\n", resultado[0], "\n\nPasos:", resultado[1],"(", resultado[0] == sorted(copia),")\n")

'''
pruebas = 50
cant = 500
for j in range(0,cant):
    valores = [i for i in range(j)]
    copia = valores[:]
    for i in range(pruebas):
        shuffle(valores)
        resultado = sort(valores)
        if resultado[0] != sorted(copia):
            break

   
if i < pruebas - 1:
    print("\n¡Todo marchaba relativamente bien, hasta que todo empezó a marchar relativamente mal!\nPrueba =", i,"\n")
else:
    print("\n¡OK, polisha!\nPasos =",resultado[1],"\n")
#'''