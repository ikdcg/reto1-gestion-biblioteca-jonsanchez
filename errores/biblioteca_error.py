class BibliotecaError(Exception):
    """Excepción personalizada de la biblioteca."""

    def __init__(self, mensaje, codigo_socio):
        super().__init__(mensaje)
        self.codigo_socio = codigo_socio