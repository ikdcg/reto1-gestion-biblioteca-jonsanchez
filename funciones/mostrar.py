from modelo.libro import Libro
from modelo.socio import Socio

# Mostrar todos los libros
def mostrar_libros(libros):
    for libro in libros.values():
        print("Código:", libro.codigo)
        print("Título:", libro.titulo)
        print("Autor:", libro.autor)
        print("Año:", libro.anio)
        print("Categoría:", libro.categoria)
        print("--------------------------")

# Mostrar libros disponibles
def mostrar_libros_disponibles(libros):
    for libro in libros.values():
        if libro.esta_disponible():
            print("Código:", libro.codigo)
            print("Título:", libro.titulo)
            print("Autor:", libro.autor)
            print("--------------------------")

#Mostrar todos los socios
def mostrar_socios(socios):
    for socio in socios.values():
        print("Código:", socio.codigo)
        print("Nombre:", socio.nombre)
        print("Email:", socio.email)
        print("--------------------------")

#Mostrar socios con prestamos
def mostrar_socios_con_prestamos(socios):
    for socio in socios.values():
        if socio.tiene_libro():
            print("Libro prestado:", socio.codigo_libro)
            print("Código:", socio.codigo)
            print("Nombre:", socio.nombre)
            print("Email:", socio.email)
            print("--------------------------")