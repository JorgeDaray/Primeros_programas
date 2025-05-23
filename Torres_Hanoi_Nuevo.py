from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def designateSpace(lisE, pos, s):
    maxS = ((2 * s) +1)
    maxMid = maxS//2
    if pos == 1:
        return ((s) - (lisE - 1))
    elif pos == 2:
        return ((s*3) - (lisE - 1))
    elif pos == 3:
        return ((s*5) - (lisE - 1))
    else:
        pass

def makeMyList(tam, T1, t4):
    maxT = ((2 * (tam - 1)) + 1)
    mod = 0
    for i in range(tam):
        space = designateSpace((tam-i), 1, tam)
        temp = maxT - mod
        s = str(" " * space + "*" * temp + " " * space)
        T1.append([s, (tam - i),i])
        mod = mod + 2
    for i in range(tam):
        space = designateSpace((tam), 1, tam)
        s = str(" " * space + " " * maxT + " " * space)
        t4.append([s, (tam - i)])

def showTower(T1, T2, T3, T4):
  s = (len(T1) + len(T2) + len(T3))
  s1, s2, s3 = s,s,s
  j,k,l,contador = 0,0,0,0
  for i in range(s):
        if s1 > len(T1):
            t1 = T4[-(i+1)][0]
            s1 = s1 - 1
            contador += 1
        else:
            t1 = T1[-(j+1)][0]
            j = j+1
            contador += 1

        if s2 > len(T2):
            t2 = T4[-(i+1)][0]
            s2 = s2-1
            contador += 1
        else:
            t2 = T2[-(k+1)][0]
            k = k+1
            contador += 1

        if s3 > len(T3):
            t3 = T4[-(i+1)][0]
            s3 = s3-1
            contador += 1
        else:
            t3 = T3[-(l+1)][0]
            l=l+1
        print(t1+t2+t3)

def cambiarValor(orig, dest, T1, T2, T3, t4):
    s = (len(T1) + len(T2) + len(T3))
    if orig == 1:
        if dest == 2:
            T2.append(T1.pop())
        elif dest == 3:
            T3.append(T1.pop())
    elif orig == 2:
        if dest == 1:
            T1.append(T2.pop())
        elif dest == 3:
            T3.append(T2.pop())
    elif orig == 3:
        if dest == 1:
            T1.append(T3.pop())
        elif dest == 2:
            T2.append(T3.pop())
    clear()
    showTower(T1, T2, T3, t4)

def torre(T1, T2, T3, t4, n, nV, orig, dest = 3, sobra = 2):
    if n==1:
        sleep(.9)
        cambiarValor(orig, dest, T1, T2, T3, t4)
    else:
        torre(T1, T2, T3, t4, n-1, nV, orig, sobra, dest)
        torre(T1, T2, T3, t4, 1, nV, orig, dest, sobra)
        torre(T1, T2, T3, t4, n-1, nV, sobra, dest, orig)

T1 = []
T2 = []
T3 = []
t4 = []

while True:
    try:
        tam = int(input("Numero de discos: "))
        break
    except:
        print("Que sea un numero entero, de favor")
makeMyList(tam, T1, t4)

clear()
showTower(T1, T2, T3, t4)

torre(T1, T2, T3, t4, tam, tam, 1)