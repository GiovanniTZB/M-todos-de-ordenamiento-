def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

edades = [25, 18, 30, 21, 19, 27]
print("Original:", edades)
print("Ordenada:", insercion(edades.copy()))
