
def resolver(actividades):
    ordenadas = sorted(
        enumerate(actividades),
        key=lambda actividad: actividad[1][0]
    )

    resultado = [""] * len(actividades)
    fin_c = 0
    fin_j = 0

    for indice, (inicio, fin) in ordenadas:
        if inicio >= fin_c:
            resultado[indice] = "C"
            fin_c = fin
        elif inicio >= fin_j:
            resultado[indice] = "J"
            fin_j = fin
        else:
            return "IMPOSSIBLE"

    return "".join(resultado)


with open("Entrada.txt", "r") as archivo:
    cantidad_casos = int(archivo.readline())

    for caso in range(1, cantidad_casos + 1):
        n = int(archivo.readline())
        actividades = []

        for _ in range(n):
            inicio, fin = map(int, archivo.readline().split())
            actividades.append((inicio, fin))

        resultado = resolver(actividades)
        print(f"Case #{caso}: {resultado}")
