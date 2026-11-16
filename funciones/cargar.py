from modelo.libro import Libro
from modelo.socio import Socio


# Cargar los libros

def cargar_libros(ruta):

    libros = {}

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea:
                datos = linea.split(";")

                codigo, titulo, autor, anio, categoria = datos[:5]

                codigo_socio = None

                if len(datos) == 6 and datos[5].strip():
                    codigo_socio = datos[5].strip()

                libro = Libro(
                    codigo.strip(),
                    titulo.strip(),
                    autor.strip(),
                    anio.strip(),
                    categoria.strip(),
                    codigo_socio
                )

                libros[codigo.strip()] = libro

    return libros



# Cargar los socios
def cargar_socios(ruta):

    socios = {}

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea:
                codigo, nombre, email, codigo_libro = linea.split(";")

                codigo = codigo.strip()
                codigo_libro = codigo_libro.strip()

                if codigo_libro == "":
                    codigo_libro = None

                socio = Socio(codigo, nombre, email, codigo_libro)

                socios[codigo] = socio

    return socios