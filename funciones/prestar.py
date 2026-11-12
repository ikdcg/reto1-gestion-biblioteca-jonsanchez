from modelo.libro import Libro
from modelo.socio import Socio
from errores.biblioteca_error import BibliotecaError
from funciones.registro import registrar_evento


# Prestar un libro a un socio
def prestar_libro(libros, socios, codigo_libro, codigo_socio):

    if codigo_libro not in libros:
        print("El libro no existe")
        return

    if codigo_socio not in socios:
        print("El socio no existe")
        return

    libro = libros[codigo_libro]
    socio = socios[codigo_socio]

    if socio.tiene_libro():
        raise BibliotecaError(
            "El socio ya tiene un libro prestado",
            codigo_socio
        )

    if not libro.esta_disponible():
        print("El libro ya está prestado")
        return

    libro.codigo_socio = codigo_socio
    socio.codigo_libro = codigo_libro

    print("Préstamo realizado correctamente.")

    registrar_evento(
        "PRESTAMO",
        f"Libro {codigo_libro} prestado al socio {codigo_socio}"
    )

    