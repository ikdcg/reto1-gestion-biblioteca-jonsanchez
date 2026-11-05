from modelo.libro import Libro
from modelo.socio import Socio

# Añadir un libro
def anadir_libro(libros, libro):

    if libro.codigo in libros:
        print("El libro ya existe.")
    else:
        libros[libro.codigo] = libro
        print("Libro añadido correctamente.")


# Añadir un socio
def anadir_socio(socios, socio):

    if socio.codigo in socios:
        print("El socio ya existe.")
    else:
        socios[socio.codigo] = socio
        print("Socio añadido correctamente.")
