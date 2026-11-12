from modelo.libro import Libro
from modelo.socio import Socio


# Guardar los libros
def guardar_libros(ruta, libros):

    with open(ruta, "w", encoding="utf-8") as f:
        for libro in libros.values():

            codigo_socio = libro.codigo_socio

            if codigo_socio is None:
                codigo_socio = ""

            linea = f"{libro.codigo};{libro.titulo};{libro.autor};{libro.anio};{libro.categoria};{codigo_socio}"

            f.write(linea)


# Guardar los socios
def guardar_socios(ruta, socios):

    with open(ruta, "w", encoding="utf-8") as f:
        for socio in socios.values():

            codigo_libro = socio.codigo_libro

            if codigo_libro is None:
                codigo_libro = ""

            linea = f"{socio.codigo};{socio.nombre};{socio.email};{codigo_libro}\n"

            f.write(linea)
