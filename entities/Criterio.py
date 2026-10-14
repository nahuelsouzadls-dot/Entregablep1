from exceptions.ErrorLaboratorio import ErrorLaboratorio


class Criterio:
    """Criterio de evaluación con un peso que indica su importancia."""

    def __init__(self, codigo, nombre, peso):
        if nombre.strip() == "":
            raise ErrorLaboratorio("El nombre del criterio no puede estar vacío.")
        if peso <= 0:
            raise ErrorLaboratorio("El peso del criterio debe ser mayor a 0.")
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.peso = peso

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - Peso: {self.peso}"
