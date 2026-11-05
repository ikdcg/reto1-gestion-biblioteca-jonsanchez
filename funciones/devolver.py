from modelo.libro import Libro
from modelo.socio import Socio
from funciones.registro import registrar_evento


# Devolver un libro
def devolver_libro(libros, socios, codigo_socio):

    if codigo_socio not in socios:
        print("El socio no existe.")
        return

    socio = socios[codigo_socio]

    if not socio.tiene_libro():
        print("El socio no tiene ningún libro prestado.")
        return

    codigo_libro = socio.codigo_libro
    libro = libros[codigo_libro]

    libro.codigo_socio = None
    socio.codigo_libro = None

    print("Libro devuelto correctamente.")

    registrar_evento(
        "DEVOLUCION",
        f"Libro {codigo_libro} devuelto por socio {codigo_socio}"
    )