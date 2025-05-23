nombre = 'x'
while nombre:
    nombre = input('Introduce una palabra en minusculas: ')
    if nombre:
        vocales = 0
        for letra in nombre:
            if letra in 'aeiou':
                vocales += 1
        print('Tu palabra tiene', vocales, 'vocales')








