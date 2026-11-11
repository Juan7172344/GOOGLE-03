def resolver(dados):
    dados.sort()
    escalera = 0

    for dado in dados:
        if dado > escalera:
            escalera += 1

    return escalera


with open("Entrada.txt", "r") as archivo:
    cantidad_casos = int(archivo.readline())

    for caso in range(1, cantidad_casos + 1):
        n = int(archivo.readline())
        dados = list(map(int, archivo.readline().split()))

        resultado = resolver(dados)
        print(f"Case #{caso}: {resultado}")