from abc import ABC, abstractmethod

from exceptions.ErrorLaboratorio import ErrorLaboratorio

PUNTAJE_MINIMO = 0
PUNTAJE_MAXIMO = 10


class OpcionIA(ABC):
    """Opción de IA genérica. Cada tipo concreto sabe calcular su costo."""

    def __init__(self, codigo, nombre):
        if nombre.strip() == "":
            raise ErrorLaboratorio("El nombre de la opción no puede estar vacío.")
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.puntajes = {}  # codigo del criterio -> puntaje

    def asignar_puntaje(self, cod_criterio, puntaje):
        if puntaje < PUNTAJE_MINIMO or puntaje > PUNTAJE_MAXIMO:
            raise ErrorLaboratorio(
                f"El puntaje debe estar entre {PUNTAJE_MINIMO} y {PUNTAJE_MAXIMO}."
            )
        self.puntajes[cod_criterio] = puntaje

    @abstractmethod
    def costo_estimado(self):
        pass

    def __str__(self):
        return (
            f"[{self.codigo}] {self.nombre} - "
            f"Costo mensual: {self.costo_estimado():.2f} USD"
        )


class ServicioAPI(OpcionIA):
    """Opción que se paga según la cantidad de consultas."""

    def __init__(self, codigo, nombre, costo_por_1000, consultas_estimadas):
        super().__init__(codigo, nombre)
        if costo_por_1000 < 0:
            raise ErrorLaboratorio("El costo por 1000 consultas no puede ser negativo.")
        if consultas_estimadas < 0:
            raise ErrorLaboratorio("Las consultas estimadas no pueden ser negativas.")
        self.costo_por_1000 = costo_por_1000
        self.consultas_estimadas = consultas_estimadas

    def costo_estimado(self):
        return (self.consultas_estimadas / 1000) * self.costo_por_1000

    def __str__(self):
        return super().__str__() + " (Servicio API)"


class PlanMensual(OpcionIA):
    """Opción que se paga por usuario por mes."""

    def __init__(self, codigo, nombre, usuarios, costo_por_usuario):
        super().__init__(codigo, nombre)
        if usuarios <= 0:
            raise ErrorLaboratorio("La cantidad de usuarios debe ser mayor a 0.")
        if costo_por_usuario < 0:
            raise ErrorLaboratorio("El costo por usuario no puede ser negativo.")
        self.usuarios = usuarios
        self.costo_por_usuario = costo_por_usuario

    def costo_estimado(self):
        return self.usuarios * self.costo_por_usuario

    def __str__(self):
        return super().__str__() + " (Plan Mensual)"
