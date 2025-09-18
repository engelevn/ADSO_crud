def suma(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def resta(a: float, b: float) -> float:
    """Resta dos números."""
    return a - b

def multiplicacion(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b

def division(a: float, b: float) -> float:
    """Divide dos números."""
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def potencia(a: float, b: float) -> float:
    """Calcula a elevado a la b."""
    return a ** b


# Menú principal
if __name__ == "__main__":
    print("Calculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")

    opcion = input("Selecciona una opción (1-5): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", suma(num1, num2))
    elif opcion == "2":
        print("Resultado:", resta(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == "4":
        print("Resultado:", division(num1, num2))
    elif opcion == "5":
        print("Resultado:", potencia(num1, num2))
    else:
        print("Opción no válida")
