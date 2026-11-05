from modelo.libro import Libro
from modelo.socio import Socio

#Prestar un libro a un socio
def prestar_libro(libros, socios, codigo_libro, codigo_socio):

    if codigo_libro not in libros:
        print("El libro no existe")
        return
    
    if codigo_socio not in socios:
        print ("El socio no existe")
        return
    
    libro=libros[codigo_libro]
    socio=socios[codigo_socio]

    if socio.tiene_libro():
        print("El socio ya tiene un libro prestado")
        return
    
    if libro.esta_disponible():
        print("El libro ya esta prestado")
        return
    
    libro.codigo_socio = codigo_socio
    socio.codigo_libro = codigo_libro

    print("Préstamo realizado correctamente.")