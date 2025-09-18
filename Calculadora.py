# Calculadora básica en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre 0"

# Menú de opciones
print("=== Calculadora Básica ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1-4): ")

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
else:
    print("Opción no válida")
