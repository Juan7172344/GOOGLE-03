
def resolver(x, y, cadena):
    infinito = float("inf")

    costo_c = 0 if cadena[0] != "J" else infinito
    costo_j = 0 if cadena[0] != "C" else infinito

    for caracter in cadena[1:]:
        nuevo_c = infinito
        nuevo_j = infinito

        if caracter != "J":
            nuevo_c = min(costo_c, costo_j + y)

        if caracter != "C":
            nuevo_j = min(costo_j, costo_c + x)

        costo_c = nuevo_c
        costo_j = nuevo_j

    return min(costo_c, costo_j)

with open("Entrada.txt", "r") as archivo:
    cantidad_casos = int(archivo.readline())

    for caso in range(1, cantidad_casos + 1):
        datos = archivo.readline().split()

        x = int(datos[0])
        y = int(datos[1])
        cadena = datos[2]

        resultado = resolver(x, y, cadena)
        print(f"Case #{caso}: {resultado}")
