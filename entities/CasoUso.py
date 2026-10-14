from exceptions.ErrorLaboratorio import ErrorLaboratorio


class CasoUso:
    """Caso de uso con un presupuesto mensual y un puntaje mínimo exigido."""

    def __init__(self, codigo, nombre, presupuesto, puntaje_minimo):
        if nombre.strip() == "":
            raise ErrorLaboratorio("El nombre del caso de uso no puede estar vacío.")
        if puntaje_minimo < 0 or puntaje_minimo > 10:
            raise ErrorLaboratorio("El puntaje mínimo debe estar entre 0 y 10.")
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.presupuesto = 0
        self.actualizar_presupuesto(presupuesto)
        self.puntaje_minimo = puntaje_minimo

    def actualizar_presupuesto(self, nuevo_presupuesto):
        if nuevo_presupuesto < 0:
            raise ErrorLaboratorio("El presupuesto no puede ser negativo.")
        self.presupuesto = nuevo_presupuesto

    def __str__(self):
        return (
            f"[{self.codigo}] {self.nombre} - Presupuesto: {self.presupuesto:.2f} USD, "
            f"Puntaje mínimo: {self.puntaje_minimo:.2f}"
        )
