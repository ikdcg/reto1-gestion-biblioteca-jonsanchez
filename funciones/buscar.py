from modelo.libro import Libro
from modelo.socio import Socio

#Buscar libro
def buscar_libros(libros, titulo_buscar):
    encontrados = []

    for libro in libros.values():
        if titulo_buscar.lower() in libro.titulo.lower():
            encontrados.append(libro)

    return encontrados

#Buscar socio
def socios_con_libros(socios):
    socios_con_prestamos = []

    for socio in socios.values():
        if socio.tiene_libro():
            socios_con_prestamos.append(socio)

    return socios_con_prestamos