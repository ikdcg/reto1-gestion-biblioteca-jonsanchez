from funciones.anadir import anadir_libro, anadir_socio
from funciones.buscar import buscar_libros
from funciones.cargar import cargar_libros, cargar_socios
from funciones.devolver import devolver_libro
from funciones.guardar import guardar_libros, guardar_socios
from funciones.registro import registrar_evento
from errores.biblioteca_error import BibliotecaError


from funciones.mostrar import (
    mostrar_libros,
    mostrar_libros_disponibles,
    mostrar_socios,
    mostrar_socios_con_prestamos
)
from funciones.prestar import prestar_libro
from modelo.libro import Libro
from modelo.socio import Socio

libros = cargar_libros("datos/libros.txt")
socios = cargar_socios("datos/socios.txt")

registrar_evento("INICIO", "Programa iniciado correctamente")

print("Libros y socios cargados correctamente.")
opcion = ""


while opcion != "9":
    print("\n=== MENÚ BIBLIOTECA ===")
    print("1. Mostrar todos los libros")
    print("2. Mostrar todos los socios")
    print("3. Mostrar libros disponibles")
    print("4. Buscar libros por título")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Mostrar socios con libros prestados")
    print("8. Añadir libros o socios")
    print("9. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        mostrar_libros(libros)
    elif opcion=="2":
        mostrar_socios(socios)
    elif opcion == "3":
        mostrar_libros_disponibles(libros)

    elif opcion == "4":
        titulo = input("Introduce el título que quieres buscar: ")
        resultados = buscar_libros(libros, titulo)

        if resultados:
            for libro in resultados:
                print(libro.titulo, "-", libro.autor)
        else:
            print("No se han encontrado libros.")
    
    elif opcion == "5":
        codigo_libro = input("Introduce el código del libro: ")
        codigo_socio = input("Introduce el código del socio: ")
        
        try:
            prestar_libro(libros, socios, codigo_libro, codigo_socio)
        except BibliotecaError as error:
            print("Error:",error)
            print("Código del socio:", error.codigo_socio)
        
    elif opcion == "6":
        codigo_socio = input("Introduce el código del socio: ")

        devolver_libro(libros, socios, codigo_socio)

    elif opcion == "7":
        mostrar_socios_con_prestamos(libros, socios)

    elif opcion == "8":
        print("1. Añadir un libro")
        print("2. Añadir un socio")

        tipo = input("¿Qué quieres añadir? ")

        if tipo == "1":
            codigo = input("Código del libro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            categoria = input("Categoría: ")

            libro = Libro(codigo, titulo, autor, anio, categoria)
            anadir_libro(libros, libro)

        elif tipo == "2":
            codigo = input("Código del socio: ")
            nombre = input("Nombre: ")
            email = input("Email: ")

            socio = Socio(codigo, nombre, email)
            anadir_socio(socios, socio)

        else:
            print("Opción no válida.")
        
    elif opcion == "9":
        guardar_libros(libros, "datos/libros.txt")
        guardar_socios(socios, "datos/socios.txt")

        print("Datos guardados correctamente.")
        print("¡Hasta pronto!")

    else:
        print("Opción no válida.")