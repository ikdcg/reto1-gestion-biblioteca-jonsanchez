from modelo.libro import Libro
from modelo.socio import Socio


# Cargar los libros
def cargar_libros(ruta):

    libros = {}

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea:
                codigo, titulo, autor, anio, categoria, codigo_socio = linea.split(";")

                if codigo_socio == "":
                    codigo_socio = None

                libro = Libro(codigo, titulo, autor, anio, categoria, codigo_socio)

                libros[codigo] = libro

    return libros


# Cargar los socios
def cargar_socios(ruta):

    socios = {}

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea:
                codigo, nombre, email, codigo_libro = linea.split(";")

                if codigo_libro == "":
                    codigo_libro = None

                socio = Socio(codigo, nombre, email, codigo_libro)

                socios[codigo] = socio

    return socios