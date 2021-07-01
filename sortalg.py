def sortboth(lista):
    pasos = 0
    long = len(lista)

    if long > 1:
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
            pasos += 1

        for i in range(2,long):
            cont = 0
            while True:
                if lista[i] >= lista[i - 1 - cont]:
                    lista.insert(i - cont,lista[i])
                    del lista[i + 1]
                    break
                elif lista[i] <= lista[cont]:
                    lista.insert(cont, lista[i])
                    del lista[i + 1]
                    break
                else:
                    pasos += 1
                    cont += 1
            pasos += 1 
    return pasos 

def sortboth2(lista):
    pasos = 0
    long = len(lista)
    lista_ord = lista[:2]

    if long > 1:
        if lista_ord[0] > lista_ord[1]:
            lista_ord[0], lista_ord[1] = lista_ord[1], lista_ord[0]
            pasos += 1

        for i in range(2,long):
            cont = 0
            while True:
                if lista[i] >= lista_ord[-(cont + 1)]:
                    lista_ord.insert(len(lista_ord)-cont,lista[i])
                    break
                elif lista[i] <= lista_ord[cont]:
                    lista_ord.insert(cont, lista[i])
                    break
                else:
                    pasos += 1
                    cont += 1
            pasos += 1  
    return pasos

def sortbubble(lista):
    pasos = cont = 0
    long = len(lista) - 1

    while cont < long:
        cambio = False 
        for i in range(0,long - cont):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                cambio = True
            pasos += 1
        if not cambio:
            break
        cont += 1
    return pasos

def sortcocktail(lista):
    pasos = cont = 0
    direccion = -1
    long = len(lista) - 1

    while cont < long:
        cambio = False
        if direccion == -1:
            inicio = cont
            fin = long - cont
        else:
            inicio = long - cont - 1
            fin = cont
        direccion *= -1
        for i in range(inicio,fin,direccion):
            if direccion == 1:
                evaluar = lista[i] > lista[i + 1]
            else:
                evaluar = lista[i] < lista[i - 1]
            if evaluar:
                lista[i], lista[i + direccion] = lista[i + direccion], lista[i]
                cambio = True
            pasos += 1
        if not cambio:
            break
        if direccion == -1:
            cont += 1  
    return pasos

def sortcomb(lista):
    pasos = 0
    long = len(lista)

    if long < 10:
        factor = 1.25
    elif long < 20 and long not in (14, 17):
        factor = 1.2
    else:
        factor = 1.16

    distancia = int(long/factor)

    while distancia > 0:
        for i in range(long):
            final = i + distancia
            if final > long - 1:
                break
            if lista[i] > lista[final]:
                lista[i], lista[final] = lista[final], lista[i]
            pasos += 1
        distancia = int(distancia/factor)
    return pasos   

def sortinsert(lista):
    pasos = 0
    long = len(lista)

    for i in range(1,long):
        pos = -1
        for j in range(i-1,-1,-1):
            pasos += 1
            if lista[i] < lista[j]:
                pos = j
            else:
                break
        if pos != -1:
            lista.insert(pos,lista[i])
            del lista[i+1]
            pasos += 1    
    return pasos

def sortminmax(lista):
    pasos = 0

    for cont in range(len(lista)//2):
        long = len(lista) - cont
        if lista[cont] > lista[long - 1]:
            pos_min = long - 1 
            pos_max = cont
        else:
            pos_min = cont 
            pos_max = long - 1
        menor = lista[pos_min]
        mayor = lista[pos_max]
        for i in range(cont + 1, long - 1):
            if lista[i] > mayor:
                mayor = lista[i]
                pos_max = i
            elif lista[i] < menor:
                menor = lista[i]
                pos_min = i
            pasos += 1
        if mayor != menor:
            if pos_min != cont or pos_max != long - 1:
                lista.insert(cont, menor)
                lista.insert(long + 1, mayor)
                if pos_max > pos_min:
                    del lista[pos_min + 1]
                    del lista[pos_max]
                else:
                    del lista[pos_max + 1]
                    del lista[pos_min]
                pasos += 1    
        else:
            break       
    return pasos

def sortminmax2(lista):
    minimos = []
    maximos = []
    pasos = 0

    while len(lista) > 1:
        pos_fin = len(lista) - 1
        if lista[0] > lista [pos_fin]:
            pos_min = pos_fin
            pos_max = 0
        else:
            pos_min = 0
            pos_max = pos_fin
        mayor = lista[pos_max]
        menor = lista[pos_min]
        for i in range(1, pos_fin):
            if lista[i] > mayor:
                mayor = lista[i]
                pos_max = i
            elif lista[i] < menor:
                menor = lista[i]
                pos_min = i
            pasos += 1   
        if mayor != menor:
            minimos.append(menor)
            maximos.insert(0,mayor)
            if pos_max > pos_min:
                del lista[pos_max]
                del lista[pos_min]       
            else:
                del lista[pos_min]
                del lista[pos_max]
            pasos += 1          
        else:
            break
    return pasos

def sortselect(lista):
    pasos = 0
    long = len(lista)

    for cont in range(long):
        pos_menor = cont
        menor = lista[cont]
        rep = 1
        for i in range(cont + 1, long):
            if lista[i] < menor:
                menor = lista[i]
                pos_menor = i
            elif lista[i] == menor:
                rep += 1
            pasos += 1    
        if rep != long:
            if pos_menor != cont:
                del lista[pos_menor]
                lista.insert(cont,menor)
                pasos += 1
        else:
            break     
    return pasos

def sortselect2(lista):
    lista_ord = []
    pasos = 0

    while len(lista):
        long = len(lista)
        pos_menor = 0
        menor = lista[0]
        rep = 1
        for i in range(1, long):
            if lista[i] < menor:
                menor = lista[i]
                pos_menor = i
            elif lista[i] == menor:
                rep += 1
            pasos += 1        
        if rep != long:
            lista_ord.append(menor)
            del lista[pos_menor] 
            pasos += 1       
        else:
            lista_ord += lista
            break    
    return pasos

from random import shuffle, randrange

tamano = 500
veces = 100
#lista = [i for i in range(tamano)]
#lista = [i for i in range(tamano,0,-1)]
#lista = [1 for i in range(tamano//2)] + [0 for i in range(tamano//2)]
lista = [randrange(0,tamano) for i in range(tamano)]
totales = [0 for i in range(tamano//10)]
#print(lista,len(lista),sep = "\n")

for i in range(veces):
    #shuffle(lista)
    for j in range(0,tamano//10):
        totales[j] += sortboth(lista[:(j + 1) * 10])
        
for suma in totales:
    print(suma//veces)