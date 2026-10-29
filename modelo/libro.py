class Libro:
    """Representa un libro de la biblioteca."""

    def __init__(self, codigo, titulo, autor, anio, categoria, codigo_socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_socio = codigo_socio

    def esta_disponible(self):
        """Devuelve True si el libro no está prestado a nadie."""
        return self.codigo_socio is None 