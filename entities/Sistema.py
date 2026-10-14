from entities.Criterio import Criterio
from entities.OpcionIA import ServicioAPI, PlanMensual
from entities.CasoUso import CasoUso
from entities.Evaluacion import Evaluacion
from exceptions.ErrorLaboratorio import ErrorLaboratorio


class Sistema:
    """Clase principal que guarda y administra todos los datos del laboratorio."""

    def __init__(self):
        self.opciones = []
        self.criterios = []
        self.casos = []
        self.evaluaciones = []
        self.proximo_cod_criterio = 1
        self.proximo_cod_opcion = 1
        self.proximo_cod_caso = 1
        self.proximo_cod_evaluacion = 1

    # ---------- Criterios ----------

    def verificar_puede_agregar_criterio(self):
        if len(self.opciones) > 0:
            raise ErrorLaboratorio(
                "No se pueden agregar criterios porque ya hay opciones de IA registradas."
            )

    def registrar_criterio(self, nombre, peso):
        self.verificar_puede_agregar_criterio()
        for criterio in self.criterios:
            if criterio.nombre.lower() == nombre.strip().lower():
                raise ErrorLaboratorio(f"Ya existe un criterio llamado '{nombre}'.")
        criterio = Criterio(self.proximo_cod_criterio, nombre, peso)
        self.criterios.append(criterio)
        self.proximo_cod_criterio += 1
        return criterio

    # ---------- Opciones de IA ----------

    def verificar_puede_agregar_opcion(self, nombre):
        if len(self.criterios) == 0:
            raise ErrorLaboratorio("Primero debe registrar al menos un criterio.")
        for opcion in self.opciones:
            if opcion.nombre.lower() == nombre.strip().lower():
                raise ErrorLaboratorio(f"Ya existe una opción llamada '{nombre}'.")

    def registrar_servicio_api(self, nombre, costo_por_1000, consultas_estimadas, puntajes):
        self.verificar_puede_agregar_opcion(nombre)
        opcion = ServicioAPI(self.proximo_cod_opcion, nombre, costo_por_1000, consultas_estimadas)
        self.agregar_opcion(opcion, puntajes)
        return opcion

    def registrar_plan_mensual(self, nombre, usuarios, costo_por_usuario, puntajes):
        self.verificar_puede_agregar_opcion(nombre)
        opcion = PlanMensual(self.proximo_cod_opcion, nombre, usuarios, costo_por_usuario)
        self.agregar_opcion(opcion, puntajes)
        return opcion

    def agregar_opcion(self, opcion, puntajes):
        # puntajes es un diccionario {cod_criterio: puntaje}
        for criterio in self.criterios:
            if criterio.codigo not in puntajes:
                raise ErrorLaboratorio(f"Falta el puntaje del criterio '{criterio.nombre}'.")
            opcion.asignar_puntaje(criterio.codigo, puntajes[criterio.codigo])
        self.opciones.append(opcion)
        self.proximo_cod_opcion += 1

    # ---------- Casos de uso ----------

    def registrar_caso(self, nombre, presupuesto, puntaje_minimo):
        for caso in self.casos:
            if caso.nombre.lower() == nombre.strip().lower():
                raise ErrorLaboratorio(f"Ya existe un caso de uso llamado '{nombre}'.")
        caso = CasoUso(self.proximo_cod_caso, nombre, presupuesto, puntaje_minimo)
        self.casos.append(caso)
        self.proximo_cod_caso += 1
        return caso

    def buscar_caso(self, codigo):
        for caso in self.casos:
            if caso.codigo == codigo:
                return caso
        raise ErrorLaboratorio(f"No existe un caso de uso con código {codigo}.")

    def actualizar_presupuesto(self, cod_caso, nuevo_presupuesto):
        caso = self.buscar_caso(cod_caso)
        caso.actualizar_presupuesto(nuevo_presupuesto)
        for evaluacion in self.evaluaciones_de_caso(cod_caso):
            evaluacion.recalcular_estado(self.criterios)
        return caso

    # ---------- Evaluaciones ----------

    def buscar_evaluacion(self, opcion, caso):
        for evaluacion in self.evaluaciones:
            if evaluacion.opcion == opcion and evaluacion.caso == caso:
                return evaluacion
        return None

    def comparar_opciones(self, cod_caso):
        caso = self.buscar_caso(cod_caso)
        if len(self.opciones) == 0:
            raise ErrorLaboratorio("No hay opciones de IA registradas para comparar.")
        resultado = []
        for opcion in self.opciones:
            evaluacion = self.buscar_evaluacion(opcion, caso)
            if evaluacion is None:
                evaluacion = Evaluacion(self.proximo_cod_evaluacion, opcion, caso, self.criterios)
                self.evaluaciones.append(evaluacion)
                self.proximo_cod_evaluacion += 1
            else:
                evaluacion.recalcular_estado(self.criterios)
            resultado.append(evaluacion)
        return resultado

    def evaluaciones_de_caso(self, cod_caso):
        caso = self.buscar_caso(cod_caso)
        resultado = []
        for evaluacion in self.evaluaciones:
            if evaluacion.caso == caso:
                resultado.append(evaluacion)
        return resultado

    def ranking_de_caso(self, cod_caso):
        evaluaciones = self.evaluaciones_de_caso(cod_caso)
        if len(evaluaciones) == 0:
            raise ErrorLaboratorio(
                "El caso todavía no tiene evaluaciones. Primero compare las opciones."
            )
        # Mayor puntaje primero; si empatan, gana la más barata.
        return sorted(
            evaluaciones,
            key=lambda e: (-e.puntaje_total(self.criterios), e.costo_total()),
        )
