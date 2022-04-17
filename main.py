import random

while True:
    nombre_mystere = int(random.randint(1, 100))

    nombre_entre = int(input('Entrez un nombre'))

    if nombre_mystere > nombre_entre:
        print("Plus")
        print(nombre_mystere, nombre_entre)
    elif nombre_entre < nombre_mystere:
        print("Moins")
        print(nombre_mystere, nombre_entre)
    else:
        print("Bravo")
        print(nombre_mystere, nombre_entre)

