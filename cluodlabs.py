import sys

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Input inválido. Por favor ingrese un número válido.")

def circuit_analysis():
    print("Análisis de Circuito - Análisis Nodal\n")
    
    # Obtener datos
    R1 = get_float_input("Ingrese el valor de Resistencia R1 (Ω): ")
    R2 = get_float_input("Ingrese el valor de Resistencia R2 (Ω): ")
    R3 = get_float_input("Ingrese el valor de Resistencia R3 (Ω): ")
    R4 = get_float_input("Ingrese el valor de Resistencia R4 (Ω): ")
    R5 = get_float_input("Ingrese el valor de Resistencia R5 (Ω): ")
    currentSource = get_float_input("Ingrese el valor de la Corriente de Fuente I(t) (A): ")
    dependentVoltageSourceFactor = get_float_input("Ingrese el factor de Fuente de Voltaje Dependiente (VR2): ")

    # Validaciones simples
    resistors = [R1, R2, R3, R4, R5]
    if any(r <= 0 for r in resistors):
        print("Error: Todos los valores de resistencias deben ser positivos y mayores que cero.")
        sys.exit(1)

    try:
        # Coeficientes nodales (igual que en React)
        coeffBV_VB = (1 / R1) - (dependentVoltageSourceFactor / R1) + (1 / R2) + (1 / R3)
        coeffBV_VC = (dependentVoltageSourceFactor / R1) - (1 / R2)

        coeffCV_VB = -1 / R2
        coeffCV_VC = (1 / R2) + (1 / R5)
        coeffCV_VE = -1 / R5

        coeffEV_VC = -1 / R5
        coeffEV_VE = (1 / R5) + (1 / R4)

        if coeffBV_VB == 0:
            print("Error: No se puede resolver: división por cero en coeficiente de VB. Revise sus entradas.")
            sys.exit(1)

        new_coeffCV_VC = coeffCV_VC - (coeffCV_VB * coeffBV_VC / coeffBV_VB)
        new_rhs_CV = currentSource

        if coeffEV_VE == 0:
            print("Error: No se puede resolver: división por cero en coeficiente de VE. Revise sus entradas.")
            sys.exit(1)

        determinant = (new_coeffCV_VC * coeffEV_VE) - (coeffCV_VE * coeffEV_VC)

        if determinant == 0:
            print("Error: Determinante cero, circuito singular o sin solución única.")
            sys.exit(1)

        VC = ((new_rhs_CV * coeffEV_VE) - (coeffCV_VE * (-currentSource))) / determinant
        VE = ((new_coeffCV_VC * (-currentSource)) - (new_rhs_CV * coeffEV_VC)) / determinant

        VB = -(coeffBV_VC / coeffBV_VB) * VC
        VA = dependentVoltageSourceFactor * (VB - VC)

        # Voltajes en resistores y potencias
        VR1 = VA - VB
        PR1 = (VR1 ** 2) / R1

        VR2 = VB - VC
        PR2 = (VR2 ** 2) / R2

        VR3 = VB - 0  # VD es tierra
        PR3 = (VR3 ** 2) / R3

        VR4 = VE - 0  # VD es tierra
        PR4 = (VR4 ** 2) / R4

        VR5 = VC - VE
        PR5 = (VR5 ** 2) / R5

        totalPower = PR1 + PR2 + PR3 + PR4 + PR5

        # Mostrar resultados
        print("\nResultados del análisis nodal:")
        print(f"VA = {VA:.3f} V")
        print(f"VB = {VB:.3f} V")
        print(f"VC = {VC:.3f} V")
        print(f"VE = {VE:.3f} V\n")

        print("Detalles de resistencias:")
        print(f"{'Resistor':<10} {'Resistencia (Ω)':<18} {'Voltaje (V)':<15} {'Potencia (W)':<15}")
        print("-" * 60)
        print(f"{'R1':<10} {R1:<18.3f} {VR1:<15.3f} {PR1:<15.3f}")
        print(f"{'R2':<10} {R2:<18.3f} {VR2:<15.3f} {PR2:<15.3f}")
        print(f"{'R3':<10} {R3:<18.3f} {VR3:<15.3f} {PR3:<15.3f}")
        print(f"{'R4':<10} {R4:<18.3f} {VR4:<15.3f} {PR4:<15.3f}")
        print(f"{'R5':<10} {R5:<18.3f} {VR5:<15.3f} {PR5:<15.3f}")

        print(f"\nPotencia total consumida en el circuito: {totalPower:.3f} W")

    except Exception as e:
        print(f"Error en el cálculo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    circuit_analysis()

