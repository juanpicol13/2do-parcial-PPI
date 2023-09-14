#Conversión de Temperatura: Crea un programa en pseudocódigo que permita convertir 
#entre Celsius y Fahrenheit. Crea dos funciones modulares: una para convertir de Celsius a 
#Fahrenheit y otra para convertir de Fahrenheit a Celsius.

# Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Programa principal

#se da a elegir entre dos opciones, convertir a fahrenheint o a celcius 
print("Elige una opción:")
print("1. Convertir de Celsius a Fahrenheit")
print("2. Convertir de Fahrenheit a Celsius")

opcion = int(input())
# si la opcion es 1, se pide ingresar los grados y se llama a su respectiva funcion 
if opcion == 1:
    temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    print("La temperatura en grados Fahrenheit es:", temperatura_fahrenheit)
    # si la opcion es 2, se pide ingresar los grados y se llama a su respectiva funcion tambien 
elif opcion == 2:
    temperatura_fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
    temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
    print("La temperatura en grados Celsius es:", temperatura_celsius)
    # si se pone otro numero que no este en las opciones, sale error 
else:
    print("Opción no válida")