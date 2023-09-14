#Calculadora Modular: Crea un programa que permita realizar operaciones matemáticas 
#básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada 
#operación
# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

# Programa principal
# se hace al usuario ingresar 2 numeros 
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

#se hace elegir que operacion desea realizar 

print("Elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingresa el número de la operación deseada: "))
# se realiza la operación elegida 

if opcion == 1:
    resultado = suma(num1, num2)
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    resultado = resta(num1, num2)
    print("El resultado de la resta es:", resultado)
elif opcion == 3:
    resultado = multiplicacion(num1, num2)
    print("El resultado de la multiplicación es:", resultado)
elif opcion == 4:
    resultado = division(num1, num2)
    print("El resultado de la división es:", resultado)
else:
    print("Opción no válida")