from datetime import datetime

RECOMENDADA = "Recomendada"
FUERA_DE_PRESUPUESTO = "Fuera de presupuesto"
PUNTAJE_INSUFICIENTE = "Puntaje insuficiente"


class Evaluacion:
    """Resultado de evaluar una opción de IA para un caso de uso."""

    def __init__(self, codigo, opcion, caso, criterios):
        self.codigo = codigo
        self.opcion = opcion
        self.caso = caso
        self.fecha = datetime.now()
        self.estado = ""
        self.recalcular_estado(criterios)

    def puntaje_total(self, criterios):
        suma_ponderada = 0
        suma_pesos = 0
        for criterio in criterios:
            puntaje = self.opcion.puntajes.get(criterio.codigo, 0)
            suma_ponderada += puntaje * criterio.peso
            suma_pesos += criterio.peso
        if suma_pesos == 0:
            return 0
        return suma_ponderada / suma_pesos

    def costo_total(self):
        return self.opcion.costo_estimado()

    def recalcular_estado(self, criterios):
        # Solo cambia el estado; la fecha original de la evaluación se conserva.
        if self.costo_total() > self.caso.presupuesto:
            self.estado = FUERA_DE_PRESUPUESTO
        elif self.puntaje_total(criterios) < self.caso.puntaje_minimo:
            self.estado = PUNTAJE_INSUFICIENTE
        else:
            self.estado = RECOMENDADA

    def mostrar(self, criterios):
        return (
            f"[{self.codigo}] {self.opcion.nombre} | "
            f"Puntaje: {self.puntaje_total(criterios):.2f} | "
            f"Costo: {self.costo_total():.2f} USD | "
            f"Estado: {self.estado} | "
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}"
        )
