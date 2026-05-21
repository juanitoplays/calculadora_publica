# Funciones de la calculadora

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
        return "Error: no se puede dividir entre 0"

def potencia(a, b):
    return a ** b


# Programa principal

print("===== CALCULADORA MODULAR =====")

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

print("\nSelecciona una opcion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Potencia")

opcion = int(input("Opcion: "))

if opcion == 1:
    print("Resultado:", suma(num1, num2))

elif opcion == 2:
    print("Resultado:", resta(num1, num2))

elif opcion == 3:
    print("Resultado:", multiplicacion(num1, num2))

elif opcion == 4:
    print("Resultado:", division(num1, num2))

elif opcion == 5:
    print("Resultado:", potencia(num1, num2))

else:
    print("Opcion no valida")