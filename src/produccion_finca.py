"""
Taller Semana 8
Ejercicios practicos de logica y resolucion de problemas; ejecucion de programas.

Caso: Una finca registra durante varios dias la produccion de leche y maiz.
El programa calcula totales, promedios y genera alertas basicas.

Competencias trabajadas:
- Analisis de problema.
- Uso de variables.
- Uso de ciclos.
- Uso de condicionales.
- Ejecucion de programas.
- Verificacion de resultados.
- Ajuste de procedimientos.
"""


def leer_numero_positivo(mensaje):
    """Solicita un numero positivo o cero. Repite hasta recibir un dato valido."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: el valor no puede ser negativo. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("Error: debe ingresar un numero valido. Ejemplo: 12 o 12.5")


def mostrar_alerta_promedio(nombre_producto, promedio, limite):
    """Muestra una alerta si el promedio esta por debajo del limite esperado."""
    if promedio < limite:
        print(f"ALERTA: el promedio de {nombre_producto} esta bajo. Revise el proceso productivo.")
    else:
        print(f"OK: el promedio de {nombre_producto} es estable segun el limite definido.")


def main():
    print("============================================")
    print("TALLER SEMANA 8 - PRODUCCION DE LA FINCA")
    print("============================================")
    print("Este programa calcula total y promedio de leche y maiz.")
    print("Tambien genera alertas si el promedio es menor al limite esperado.\n")

    dias = int(leer_numero_positivo("Ingrese el numero de dias a registrar: "))

    while dias == 0:
        print("Debe registrar al menos 1 dia para calcular resultados.")
        dias = int(leer_numero_positivo("Ingrese el numero de dias a registrar: "))

    total_leche = 0
    total_maiz = 0

    for dia in range(1, dias + 1):
        print(f"\nDia {dia}")
        leche = leer_numero_positivo("Ingrese litros de leche producidos: ")
        maiz = leer_numero_positivo("Ingrese kilos de maiz cosechados: ")

        total_leche = total_leche + leche
        total_maiz = total_maiz + maiz

    promedio_leche = total_leche / dias
    promedio_maiz = total_maiz / dias

    print("\n========== RESULTADOS ==========")
    print(f"Dias registrados: {dias}")
    print(f"Total de leche: {total_leche:.2f} litros")
    print(f"Promedio diario de leche: {promedio_leche:.2f} litros")
    print(f"Total de maiz: {total_maiz:.2f} kilos")
    print(f"Promedio diario de maiz: {promedio_maiz:.2f} kilos")

    print("\n========== ALERTAS ==========")
    mostrar_alerta_promedio("leche", promedio_leche, 8)
    mostrar_alerta_promedio("maiz", promedio_maiz, 20)

    print("\nProceso finalizado. Revise si los resultados coinciden con sus calculos manuales.")


if __name__ == "__main__":
    main()
