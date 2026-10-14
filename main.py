from entities.Sistema import Sistema
from exceptions.ErrorLaboratorio import ErrorLaboratorio


# ---------- Funciones auxiliares de entrada ----------

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("  El valor no puede estar vacío. Intente de nuevo.")


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero. Intente de nuevo.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  El valor debe ser mayor o igual a {minimo}. Intente de nuevo.")
        elif maximo is not None and valor > maximo:
            print(f"  El valor debe ser menor o igual a {maximo}. Intente de nuevo.")
        else:
            return valor


def pedir_decimal(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número. Intente de nuevo.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  El valor debe ser mayor o igual a {minimo}. Intente de nuevo.")
        elif maximo is not None and valor > maximo:
            print(f"  El valor debe ser menor o igual a {maximo}. Intente de nuevo.")
        else:
            return valor


def elegir_caso(sistema):
    if len(sistema.casos) == 0:
        raise ErrorLaboratorio("No hay casos de uso registrados.")
    print("\nCasos de uso disponibles:")
    for caso in sistema.casos:
        print(f"  {caso}")
    codigo = pedir_entero("Ingrese el código del caso: ")
    return sistema.buscar_caso(codigo)


# ---------- Registro de datos ----------

def registrar_criterio(sistema):
    # Se verifica la regla antes de pedir los datos al usuario.
    sistema.verificar_puede_agregar_criterio()
    nombre = pedir_texto("Nombre del criterio: ")
    peso = pedir_entero("Peso del criterio (entero mayor a 0): ", minimo=1)
    criterio = sistema.registrar_criterio(nombre, peso)
    print(f"Criterio registrado: {criterio}")


def pedir_puntajes(sistema):
    puntajes = {}
    print("Ingrese el puntaje (0 a 10) para cada criterio:")
    for criterio in sistema.criterios:
        puntajes[criterio.codigo] = pedir_entero(f"  {criterio.nombre}: ", minimo=0, maximo=10)
    return puntajes


def registrar_opcion(sistema):
    nombre = pedir_texto("Nombre de la opción de IA: ")
    sistema.verificar_puede_agregar_opcion(nombre)
    print("Tipo de opción:")
    print("  1. Servicio API")
    print("  2. Plan Mensual")
    tipo = pedir_entero("Seleccione el tipo: ", minimo=1, maximo=2)

    if tipo == 1:
        costo_por_1000 = pedir_decimal("Costo por 1000 consultas (USD): ", minimo=0)
        consultas = pedir_entero("Consultas estimadas por mes: ", minimo=0)
        puntajes = pedir_puntajes(sistema)
        opcion = sistema.registrar_servicio_api(nombre, costo_por_1000, consultas, puntajes)
    else:
        usuarios = pedir_entero("Cantidad de usuarios: ", minimo=1)
        costo_por_usuario = pedir_decimal("Costo por usuario (USD): ", minimo=0)
        puntajes = pedir_puntajes(sistema)
        opcion = sistema.registrar_plan_mensual(nombre, usuarios, costo_por_usuario, puntajes)

    print(f"Opción registrada: {opcion}")


def registrar_caso(sistema):
    nombre = pedir_texto("Nombre del caso de uso: ")
    presupuesto = pedir_decimal("Presupuesto mensual (USD): ", minimo=0)
    puntaje_minimo = pedir_decimal("Puntaje mínimo exigido (0 a 10): ", minimo=0, maximo=10)
    caso = sistema.registrar_caso(nombre, presupuesto, puntaje_minimo)
    print(f"Caso de uso registrado: {caso}")


def listar(titulo, elementos):
    print(f"\n--- {titulo} ---")
    if len(elementos) == 0:
        print("  (no hay registros)")
    for elemento in elementos:
        print(f"  {elemento}")


def menu_registro(sistema):
    opcion = -1
    while opcion != 0:
        print("\n===== REGISTRO DE DATOS =====")
        print("1. Registrar criterio")
        print("2. Registrar opción de IA")
        print("3. Registrar caso de uso")
        print("4. Listar criterios")
        print("5. Listar opciones de IA")
        print("6. Listar casos de uso")
        print("0. Volver al menú principal")
        opcion = pedir_entero("Seleccione una opción: ", minimo=0, maximo=6)

        try:
            if opcion == 1:
                registrar_criterio(sistema)
            elif opcion == 2:
                registrar_opcion(sistema)
            elif opcion == 3:
                registrar_caso(sistema)
            elif opcion == 4:
                listar("Criterios", sistema.criterios)
            elif opcion == 5:
                listar("Opciones de IA", sistema.opciones)
            elif opcion == 6:
                listar("Casos de uso", sistema.casos)
        except ErrorLaboratorio as error:
            print(f"Error: {error}")


# ---------- Comparación y evaluaciones ----------

def mostrar_evaluaciones(sistema, evaluaciones):
    if len(evaluaciones) == 0:
        print("  El caso todavía no tiene evaluaciones.")
    for evaluacion in evaluaciones:
        print(f"  {evaluacion.mostrar(sistema.criterios)}")


def comparar_opciones(sistema):
    caso = elegir_caso(sistema)
    evaluaciones = sistema.comparar_opciones(caso.codigo)
    print(f"\nComparación para el caso '{caso.nombre}':")
    mostrar_evaluaciones(sistema, evaluaciones)


def listar_evaluaciones(sistema):
    caso = elegir_caso(sistema)
    print(f"\nEvaluaciones del caso '{caso.nombre}':")
    mostrar_evaluaciones(sistema, sistema.evaluaciones_de_caso(caso.codigo))


def ver_ranking(sistema):
    caso = elegir_caso(sistema)
    ranking = sistema.ranking_de_caso(caso.codigo)
    print(f"\nRanking del caso '{caso.nombre}':")
    posicion = 1
    for evaluacion in ranking:
        print(
            f"  {posicion}. {evaluacion.opcion.nombre} "
            f"(Puntaje: {evaluacion.puntaje_total(sistema.criterios):.2f}, "
            f"Costo: {evaluacion.costo_total():.2f} USD) - {evaluacion.estado}"
        )
        posicion += 1


def actualizar_presupuesto(sistema):
    caso = elegir_caso(sistema)
    nuevo = pedir_decimal(f"Nuevo presupuesto para '{caso.nombre}' (USD): ", minimo=0)
    sistema.actualizar_presupuesto(caso.codigo, nuevo)
    print(f"Presupuesto actualizado: {caso}")
    print("Los estados de las evaluaciones del caso fueron recalculados.")


# ---------- Menú principal ----------

def menu_principal():
    sistema = Sistema()
    opcion = -1
    while opcion != 0:
        print("\n===== LABORATORIO DE EVALUACIÓN DE OPCIONES DE IA =====")
        print("1. Registro de datos (criterios, opciones, casos)")
        print("2. Comparar opciones para un caso de uso")
        print("3. Listar evaluaciones de un caso de uso")
        print("4. Ver ranking de un caso de uso")
        print("5. Actualizar presupuesto de un caso de uso")
        print("0. Salir")
        opcion = pedir_entero("Seleccione una opción: ", minimo=0, maximo=5)

        try:
            if opcion == 1:
                menu_registro(sistema)
            elif opcion == 2:
                comparar_opciones(sistema)
            elif opcion == 3:
                listar_evaluaciones(sistema)
            elif opcion == 4:
                ver_ranking(sistema)
            elif opcion == 5:
                actualizar_presupuesto(sistema)
        except ErrorLaboratorio as error:
            print(f"Error: {error}")

    print("¡Hasta luego!")


if __name__ == "__main__":
    menu_principal()
