nombre = input('¿Cuál es tu nombre? ')
if nombre.isdigit():
    print('Dije nombre, no edad...')
elif nombre:
    print('Hola,',nombre)
else:
    print('No seas timido...')