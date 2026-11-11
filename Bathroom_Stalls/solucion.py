
def resolver(n, k):
    grupos = {n: 1}

    while True:
        tamaño = max(grupos)
        cantidad = grupos.pop(tamaño)

        mayor = tamaño // 2
        menor = (tamaño - 1) // 2

        if k <= cantidad:
            return mayor, menor

        k -= cantidad

        grupos[mayor] = grupos.get(mayor, 0) + cantidad
        grupos[menor] = grupos.get(menor, 0) + cantidad


with open("Entrada.txt", "r") as archivo:
    cantidad_casos = int(archivo.readline())

    for caso in range(1, cantidad_casos + 1):
        n, k = map(int, archivo.readline().split())

        mayor, menor = resolver(n, k)

        print(f"Case #{caso}: {mayor} {menor}")
