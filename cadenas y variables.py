nombre = 'x'
while nombre:
    nombre = input('¿Cuál es tu nombre? ')
    if nombre.isspace():
        print('Dije nombre, no edad...')
    elif nombre:
        print('Hola,', nombre)
        vocales = 0
        for letra in nombre:
            if letra in 'aeiou':
                vocales += 1
        print('Tu nombre tiene',vocales,'vocales')
    else:
        print('No seas timido...')