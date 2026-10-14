class ErrorLaboratorio(Exception):
    """Error propio del sistema para validaciones y reglas de negocio."""

    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje
