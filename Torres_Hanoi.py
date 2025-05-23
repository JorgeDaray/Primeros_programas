import time

def dibujarTorres():
    for fila in torres:
        for col in fila:
            if col == 0:
                print(" "*(discos+4), "*", " "*(discos+4), end="")
            else:
                print(" "*(discos-col+3), "[", "*"*(2*col-1), "]", " "*(discos-col+3), end="")
        print()
    time.sleep(1.5)


def buscarDisco(col):
	fila = 0
	while fila <= discos and torres[fila][col] == 0:
		fila += 1
	if fila <= discos:
		return torres[fila][col]
	else:
		return 0


def buscarEspacio(col):
	fila = 0
	while fila <= discos and torres[fila][col] == 0:
		fila += 1
	return fila - 1


def quitarDisco(col):
    fila = 0
    while fila <= discos and torres[fila][col] == 0:
        fila += 1
    torres[fila][col] = 0


def hanoi(n, origen=1, auxiliar=2, destino=3):

    if n > 0:
        hanoi(n-1, origen, destino, auxiliar)
        disco = buscarDisco(origen-1)
        quitarDisco(origen-1)
        torres[buscarEspacio(destino-1)][destino-1] = disco
        print("\n"*40)
        dibujarTorres()
        hanoi(n-1, auxiliar, origen, destino)


discos = int(input("Número de discos: "))
if discos > 0:
    torres = [[0, 0, 0]]
    for i in range(discos):
        torres.append([i+1, 0, 0])
    dibujarTorres()
    hanoi(discos)
else:
    print("El número de discos debe ser mayor a 0.")