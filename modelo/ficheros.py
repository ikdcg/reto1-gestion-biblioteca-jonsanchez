from modelo.libro import Libro
from modelo.socio import Socio


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

# Guardar los libros
def guardar_libros(ruta, libros):

    with open(ruta, "w", encoding="utf-8") as f:
        for libro in libros.values():

            codigo_socio = libro.codigo_socio

            if codigo_socio is None:
                codigo_socio = ""

            linea = f"{libro.codigo};{libro.titulo};{libro.autor};{libro.anio};{libro.categoria};{codigo_socio}\n"

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


def buscar_libros(libros, titulo_buscar):
    encontrados = []

    for libro in libros.values():
        if titulo_buscar.lower() in libro.titulo.lower():
            encontrados.append(libro)

    return encontrados

def socios_con_libros(socios):
    socios_con_prestamos = []

    for socio in socios.values():
        if socio.tiene_libro():
            socios_con_prestamos.append(socio)

    return socios_con_prestamos