from datetime import datetime


def registrar_evento(evento, detalles):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}][{evento}][{detalles}]\n")