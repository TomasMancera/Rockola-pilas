from pila import *
rockola = Pila()


x = 0
while (x != 4):
    try:
        x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar disco a la rockola\n2)Seleccionar disco a reproducir\n3)Ver discos en rockola.\n4)Salir\n"))
    except ValueError:
        print("El dato ingresado no esta permitido, se esperaba un entero(1-4)")
    if (x == 1):
        nombreDisco = input("Escribe el nombre del disco:\n").capitalize()
        artista = input("Escribe el nombre del Artista:\n").capitalize()
        duracion = int(input("Ingresa la duracion del disco:\n (En formato de entero y representado en segundos)\n"))
        disco = {
            "NombreDisco": nombreDisco,
            "Artista": artista,
            "Duracion": duracion
        }
        apilar(rockola, disco)
    elif (x == 2):
        print("\n===========================================\n")
        seleccionarCancion(rockola)
        print("\n===========================================\n")
    elif (x == 3):
        print("\n===========================================\n")
        verPlaylist(rockola)
        print("\n===========================================\n")
    elif (x == 4):
        print("\nEl programa fue finalizado con éxito.\n")
