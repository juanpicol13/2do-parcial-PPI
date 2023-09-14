#Búsqueda: Escribe un programa en pseudocódigo que realice una búsqueda de un número 
#dado, en un arreglo. Crea una función modular para llevar a cabo la búsqueda.
# Función para realizar una en un arreglo
def buscar_numero(arr, numero):
    for i in range(len(arr)):
        if arr[i] == numero:
            return i  # Devolver la posición donde se encontró el número
    return -1  # Devolver -1 si el número no se encuentra en el arreglo

# Programa principal
#le damos los valores al arreglo 
arr = [10, 23, 5, 17, 8, 12, 15]

#se pide al usuario que ingrese el numero que desea buscar 
numero_buscado = int(input("Ingresa el número que deseas buscar: "))
#se llama a la funcion para buscar el numero 
resultado = buscar_numero(arr, numero_buscado)
# si el resultado es distinto de -1 se muestra la posicion en que se encuentra el numero 
if resultado != -1:
    print(f"El número {numero_buscado} se encuentra en la posición {resultado} del arreglo.")
else:
    print(f"El número {numero_buscado} no se encuentra en el arreglo.")