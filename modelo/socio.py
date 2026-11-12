class Socio:
    """Representa a un socio de la biblioteca."""

    def __init__(self, codigo, nombre, email, codigo_libro=None):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.codigo_libro = codigo_libro

    def tiene_libro(self):
        """Devuelve True si el socio tiene un libro prestado."""
        return self.codigo_libro is not None