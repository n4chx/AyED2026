# Introduccion al bucle precondicional: while

#########################################
# Ejercicio 1 : Mostrar en pantalla los numeros del 1 al 50. Generar dos versiones, una con el bucle for, y otra con el bucle while. Que diferencias tienen?
#########################################
#Version con bucle for
for i in range (1, 51):
    print (i)

#Version con bucle while
i = 1
while i <= 50:
    print (i)
    i = i + 1

#########################################
# Ejercicio 2 : Mostrar en pantalla la siguiente sencuencia de valores, todos en una sola linea, separados por una coma. 10,20,30,40,50,60,70,80,90,100
#########################################
i = 10                 
while i <= 100:        
    if i == 100:       
        print(i)
    else:
        print(i, end=",")
    
    i = i + 10

#########################################
# Ejercicio 3 : Pedir 6 numeros al usuario. Almacenarlos en una lista
#########################################
numeros = []
i = 0 
while i < 6:
    n = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(n)
    i = i + 1 

#########################################
# Ejercicio 4 : Pedir al usuario 10 numeros. Almacenar solo aquellos que son pares en una lista. Mostrar los numeros pares ingresados
#########################################
numeros_pares = []
i = 0
while i < 10:
    n = int(input(f"Ingrese un numero {i+1}: "))
    if n % 2 == 0:
        numeros_pares.append(n)
    i = i + 1
print("Numeros pares ingresados:", numeros_pares)

#########################################
# Ejercicio 5 : Pedir al usuario un valor llamado n, controlar que este entre 1 y 10. Mostrar en pantalla, los valores en orden decreciente, uno por linea, desde n. 
#########################################
n = int(input("Ingrese un valor entre 1 y 10: "))
while n < 1 or n > 10:
    n = int(input("Valor no valido. Ingrese un valor entre 1 y 10: "))
while n >= 1:
    print(n)
    n = n - 1

#########################################
# Ejercicio 6 : Pedir numeros al usuario hasta que se ingrese el valor -1. sin listas ni nada, solo usar el bucle while para pedir hasta que se ingrese el valor concreto predefinido
#########################################
n = int(input("Ingrese un numero (-1 para finalizar): "))
while n != -1:
    n = int(input("Ingrese un numero (-1 para finalizar): "))

#########################################
# Ejercicio 7 : Permitir ingresar numeros enteros hasta que se ingrese la opcion "s" de salir. Mostrar todos los numeros que se ingresaron
#########################################
numeros_ingresados = []
while True:
    entrada = input("Ingrese un numero entero (o 's' para salir): ")
    if entrada.lower() == 's':
        break
    try:
        numero = int(entrada)
        numeros_ingresados.append(numero)
    except ValueError:
        print("Entrada no valida. Ingrese un numero entero o 's' para salir.")
print("Numeros ingresados:", numeros_ingresados)

#Utilizamos un bucle while True que permite ingresar numeros hasta que se ingrese 's' para salir, tambien usamos una validacion para verificar que la entrada sea un entero, caso contrario se muestra un mensaje de error y se vuelve a solicitar la entrada

#########################################
# Ejercicio 8 : Implementar un algoritmo que permita ingresar numeros hasta que se ingrese una letra q de salir, luego muestre la suma de todos los pares ingresados por un lado, y el promedio por otro
#########################################
suma_pares = 0
contador_pares = 0
while True:
    entrada = input("Ingrese un numero entero (Ingrese 'q' para salir): ")
    if entrada.lower() == 'q':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            suma_pares += numero
            contador_pares += 1
    except ValueError:
        print("Entrada no valida. Ingrese un numero entero o 'q' para salir.")