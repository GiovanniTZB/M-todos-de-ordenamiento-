def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

precios = [120.5, 80, 99.9, 45, 150, 60]
print("Original:", precios)
print("Ordenada:", seleccion(precios.copy()))
