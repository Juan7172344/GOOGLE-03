
def resolver(diversion, padres):
    n = len(diversion)

    hijos = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        hijos[padres[i - 1]].append(i)

    pendiente = [0] * (n + 1)
    total = 0

    for i in range(n, 0, -1):
        if not hijos[i]:
            pendiente[i] = diversion[i - 1]
        else:
            valores = [pendiente[hijo] for hijo in hijos[i]]
            menor = min(valores)

            total += sum(valores) - menor
            pendiente[i] = max(diversion[i - 1], menor)

    for raiz in hijos[0]:
        total += pendiente[raiz]

    return total


with open("Entrada.txt", "r") as archivo:
    cantidad_casos = int(archivo.readline())

    for caso in range(1, cantidad_casos + 1):
        n = int(archivo.readline())
        diversion = list(map(int, archivo.readline().split()))
        padres = list(map(int, archivo.readline().split()))

        resultado = resolver(diversion, padres)
        print(f"Case #{caso}: {resultado}")
