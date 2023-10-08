import time


class nodoPila(object):
    info, sig = None, None


class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamano = 0


def apilar(pila, dato):
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamano += 1


def desapilar(pila):
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamano -= 1
    return x


def pila_vacia(pila):
    return pila.cima is None


def en_cima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None


def tamano(pila):
    return pila.tamano


def barrido(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)


def verPlaylist(pila):
    if pila_vacia(pila):
        print("La playlist está vacía(No hay siguiente canción)")
    else:
        print("Discos disponibles:")

    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print("\n".join([f"{k}: {v}" for k, v in dato.items()]) + "\n")

        apilar(paux, dato)
    while not pila_vacia(paux):
        dato = desapilar(paux)
        apilar(pila, dato)


def seleccionarCancion(pila):
    if pila_vacia(pila):
        print("La rockola está vacía(No puedes seleccionar discos)")
    else:
        cancion = input("Ingresa el nombre del disco que deseas reproducir: ").capitalize()
        paux = Pila()
        cancion_encontrada = False

        while (not pila_vacia(pila)):
            dato = desapilar(pila)

            if (cancion == dato["NombreDisco"]):
                print("Disco seleccionado con éxito...")
                print("Reproduciendo canciones...")
                time.sleep(dato["Duracion"])
                print("El disco ha finalizado")
                cancion_encontrada = True

            apilar(paux, dato)


        if not cancion_encontrada:
            print(f"No se encontró el disco con el nombre {cancion}")

        while (not pila_vacia(paux)):
            dato = desapilar(paux)
            apilar(pila, dato)
