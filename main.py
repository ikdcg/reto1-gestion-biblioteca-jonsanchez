from modelo.ficheros import (
    cargar_libros,
    cargar_socios,
    guardar_libros,
    guardar_socios
)

libro =cargar_libros("datos/libros.txt")
socio=cargar_socios("datos/socios.txt")

print("Libros y socios cargados correctamente.")