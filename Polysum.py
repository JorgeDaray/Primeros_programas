import math
pi = math.pi
n = int(input("numero de lados:"))
s = float(input("longitud:"))
def Polysum(n,s):
    area = (.25*n*s**2)/(math.tan (pi/n))
    perimetro = n*s
    suma = area + (perimetro**2)
    return round(suma,4)
print(Polysum(n,s))
