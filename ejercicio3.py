 #Números Primos en un Rango: Escribe un programa en pseudocódigo que encuentre y 
 #muestre todos los números primos dentro de un rango dado. Utiliza una función modular 
# para determinar si un número es primo.

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Programa principal

#se pide ingresar los numeros donde comienza y termina el rango 
inicio = int(input("Ingresa el número de inicio del rango: "))
fin = int(input("Ingresa el número final del rango: "))

print(f"Los números primos en el rango de {inicio} a {fin} son:")
# para los numeros que se encuentran entre el principio y el final del rango, se llama a la funcion definida para verificar cuales son numeros primos 
for numero in range(inicio, fin + 1):
    #si hay numeros primos, se los escribe en pantalla, si no hay, no se muestra nada 
    if es_primo(numero):
        print(numero)