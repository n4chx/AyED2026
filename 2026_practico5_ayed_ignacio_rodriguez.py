# Funciones

#########################################
# Ejercicio 1 : Crear una funcion que tome un argumento numerico y devuelva ese numero elevado al cuadrado. Luego de haber creado la funcion, pedirle al usuario 5 numeros, de a uno, e ir mostrando cada numero elevado al cuadrado. utilizando dicha funcion
#########################################
def elevar_cuadrado(numero):
    return numero ** 2
for i in range(5):
    n = int(input(f"Ingrese un numero {i+1}: "))
    resultado = elevar_cuadrado(n)
    print(f"{n} elevado al cuadrado es: {resultado}")

#########################################
# Ejercicio 2 : Crear una funcion llamada es_positivo que tome un numero como argumento y devuelva verdadero o falso, como valores logicos, si el numero es positivo o no
#########################################
def es_positivo(numero):
    return numero > 0
n = int(input("Ingrese un numero: "))
if es_positivo(n):
    print(f"{n} es un numero positivo.")
else:
    print(f"{n} no es un numero positivo.")

#########################################
# Ejercicio 3 : Crear una funcion llamada iguales, que tome dos palabras como parametros y determine si son iguales o no. DEvolviendo verdadero si lo son o falso en caso contrario
#########################################
def iguales(palabra1, palabra2):
    return palabra1 == palabra2
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
if iguales(palabra1, palabra2):
    print("Las palabras son iguales.")
else:
    print("Las palabras no son iguales.")

#########################################
# Ejercicio 4 : Crear una funcion llamada signo, que tome un numero y devuelva 1 si este es positivo y 0 si es negativo
#########################################
def signo(numero):
    if numero > 0:
        return 1
    else:
        return 0
n = int(input("Ingrese un numero: "))
resultado = signo(n)
if resultado == 1:
    print(f"{n} es un numero positivo.")
else:
    print(f"{n} es un numero negativo.")

#########################################
# Ejercicio 5 : Crear una funcion llamada escalon, que tome un numero y devuelva 1 si este es positivo y 0 si este es negativo
#########################################
def escalon(numero):
    if numero > 0:
        return 1
    else:
        return 0
n = int(input("Ingrese un numero: "))
resultado = escalon(n)
if resultado == 1:
    print(f"{n} es un numero positivo.")
else:
    print(f"{n} es un numero negativo.")

#########################################
# Ejercicio 6 : Crear una funcion llamada delta_de_dirac que tome dos numeros enteros y devuelva 1 si ambos numeros son iguales y 0 si no
#########################################
def delta_de_dirac(num1, num2):
    if num1 == num2:
        return 1
    else:
        return 0
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
resultado = delta_de_dirac(num1, num2)
if resultado == 1:
    print("Los numeros son iguales.")
else:
    print("Los numeros no son iguales.")

#########################################
# Ejercicio 7 : Crear una funcion llamada raiz_uno que tome tres parametros, a, b y c y calcule solo la primera raiz de la funcion cuadratica
#########################################
import math
def raiz_uno(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay raices reales"
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        return raiz1
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
resultado = raiz_uno(a, b, c)
print(f"La primera raiz de la funcion cuadratica es: {resultado}")

#########################################
# Ejercicio 8 : Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva verdadero o falso, segun n pertenece o no al intervalo cerrado 
#########################################
def pertenece_intervalo(n, a, b):
    return a <= n <= b
n = float(input("Ingrese un numero n: "))
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
if pertenece_intervalo(n, a, b):
    print(f"{n} pertenece al intervalo cerrado [{a}, {b}].")
else:
    print(f"{n} no pertenece al intervalo cerrado [{a}, {b}].")

#########################################
# Ejercicio 10 : Crear una funcion que convierta una temperatura en Fahrenheit, en su temperatura equivalente, en grados Celsius. Pedirle al usuario 10 temperaturas en F y mostrar su conversion a Celsius
#########################################
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius
for i in range(10):
    f = float(input(f"Ingrese la temperatura en Fahrenheit {i+1}: "))
    c = fahrenheit_a_celsius(f)
    print(f"{f} grados Fahrenheit es igual a {c:.2f} grados Celsius.")

#########################################
# Ejercicio 11 : Crear una funcion que tome dos palabras como parametros y devuelva el texto resultante de concatenar ambas palabras
#########################################
def concatenar_palabras(palabra1, palabra2):
    return palabra1 + palabra2
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
resultado = concatenar_palabras(palabra1, palabra2)
print(f"El resultado de concatenar las palabras es: {resultado}")

#########################################
# Ejercicio 12 : A la funcion anterior, agregarle un tercer argumento y definir si debe agregar espacio o no entre las dos palabras
#########################################
def concatenar_palabras(palabra1, palabra2, espacio):
    if espacio:
        return palabra1 + " " + palabra2
    else:
        return palabra1 + palabra2
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
espacio = input("¿Desea concatenar las palabras con espacio? (s/n): ").lower() == 's'
resultado = concatenar_palabras(palabra1, palabra2, espacio)
print(f"El resultado de concatenar las palabras es: {resultado}")

#########################################
# Ejercicio 13 : Crear una funcion que tome como argumentos una frase y una letra, y determina cuantas veces esta esa letra en dicha frase
#########################################
def contar_letra(frase, letra):
    return frase.count(letra)
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra para contar en la frase: ")
resultado = contar_letra(frase, letra)
print(f"La letra '{letra}' aparece {resultado} veces en la frase.")

#########################################
# Ejercicio 14 : Crear una funcion llamada capitalizar, que tome una palabra como argumento y devuelva una palabra con la primer letra en mayusculas
#########################################
def capitalizar(palabra):
    return palabra.capitalize()
palabra = input("Ingrese una palabra: ")
resultado = capitalizar(palabra)
print(f"La palabra capitalizada es: {resultado}")

#########################################
# Ejercicio 15 : Crear una funcion que tome una lista de 2 valores numericos como argumento y devuelva la lista ordenada
#########################################
def ordenar_lista(lista):
    return sorted(lista)
lista = []
for i in range(2):
    numero = float(input(f"Ingrese el numero {i+1}: "))
    lista.append(numero)
resultado = ordenar_lista(lista)
print(f"La lista ordenada es: {resultado}")

#########################################
# Ejercicio 16 : Crear una funcion que tome dos numeros a y b y devuelva la cantidad de numeros pares que hay en ese intervalo
#########################################
def contar_pares(a, b):
    contador = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            contador += 1
    return contador
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b (debe ser mayor o igual a a): "))
while b < a:
    b = int(input("Valor no valido. Ingrese un valor de b mayor o igual a a: "))
resultado = contar_pares(a, b)
print(f"La cantidad de numeros pares en el intervalo [{a}, {b}] es: {resultado}")

#########################################
# Ejercicio 17 : Describa lo que significa que un argumento sea pasado por valor vs pasado por referencia
#########################################
# Pasar por valor significa que se pasa una copia del valor del argumento a la funcion, por lo que cualquier cambio realizado dentro de la funcion no afecta al valor original fuera de la funcion. Pasar por referencia significa que se pasa una referencia al valor del argumento, por lo que cualquier cambio realizado dentro de la funcion afecta al valor original fuera de la funcion.

#########################################
# Ejercicio 18 : En el siguiente codigo, que se considera un error o mala practica?
#########################################
def funcion_algo(a, b):
    a = 45
    return (2 * a) - b
# El error en este codigo es que se esta modificando el valor del argumento 'a' dentro de la funcion, lo cual puede causar errores si se espera que 'a' mantenga su valor original fuera de la funcion. 