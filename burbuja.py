def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista

calificaciones = [8, 5, 10, 6, 9, 7]
print("Original:", calificaciones)
print("Ordenada:", burbuja(calificaciones.copy()))
