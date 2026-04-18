# Expresiones aritmeticas, variables y tipos de datos basicos

#########################################
# Ejercicio 1 : Crear un programa que escriba ”Hola mundo” en la pantalla
#########################################

print("Hola mundo")

#########################################
# Ejercicio 2 : Guardar un numero entero en una variable, llamada n por ejemplo, y mostrarlo en pantalla.
#########################################

n = 5
print(n)

##########################################
#  Ejercicio 3 :Crear una variable llamada a y asignarle un valor. Luego imprimir en pantalla la variable A en mayusculas. ¿Que ocurrio? ¿Porque ocurrio eso?
##########################################

a = 10
print(A)
# Ocurrio un error porque la variable que esta definida es a y no A, lo que significa que distingue entre mayusculas y minusculas.

###########################################
# Ejercicio 4 : Mostrar en pantalla los resultados de calcular las siguientes expresiones (estas expresiones se encuentran escritas matematicamente, y debera reescribirlas en notacion decomputadora previamente; cada vez que encuentre en la expresion una letra minuscula, debera considerar que ese dato lo debera ingresar el usuario)
###########################################

# a) 5a + 10b
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
resultado = 5*a + 10*b
print("El resultado de la expresion 5a + 10b es: ", resultado)

# b) b^2
b = int(input("Ingrese el valor de b: "))
resultado = b**2
print("El resultado de la expresion b^2 es: ", resultado)

# c) 2n-1/2n+1
n = int(input("Ingrese el valor de n: "))
resultado = (2*n - 1) / (2*n + 1)
print("El resultado de la expresion 2n-1/2n+1 es: ", resultado)

# d) 1

# e) 2x-y
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
resultado = 2*x - y
print("El resultado de la expresion 2x-y es: ", resultado)

#f) x-y/x+y
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
resultado = (x - y) / (x + y)
print("El resultado de la expresion x-y/x+y es: ", resultado)

#################################################################################################################################
# Ingreso de datos por parte del Usuario

###########################################
# Ejercicio 5 : Permita ingresar una palabra al usuario, la computadora debera repetir la palabra que fue ingresada en pantalla.
###########################################

palabra = input("Ingrese una palabra: ")
print("La palabra ingresada es: ", palabra)

############################################
# Ejercicio 6 : Implemente un programa que lea por teclado dos numeros enteros e imprima en pantalla los valores leıdos en orden inverso. Por ejemplo, si se ingresan los numeros 4 y 8, debe mostrar el mensaje: Se ingresaron los valores 8 y 4.
#############################################

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
print("Se ingresaron los valores ", num2, " y ", num1)

############################################
# Ejercicio 7 : El usuario debera ingresar un valor numerico, y la computadora mostrara en pantalla ese numero incrementado en 1.
############################################

numero = int(input("Ingrese un numero: "))
numero_incrementado = numero + 1
print("El numero ingresado incrementado en 1 es: ", numero_incrementado)

############################################
# Ejercicio 8 : Pedir dos valores numericos. Calcular y mostrar la suma, resta, multiplicacion y division de ambos.
#############################################

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("La suma de ambos numeros es: ", suma)
print("La resta de ambos numeros es: ", resta)
print("La multiplicacion de ambos numeros es: ", multiplicacion)
print("La division de ambos numeros es: ", division)

#############################################
# Ejercicio 9 : Implemente un programa que lea dos numeros reales e imprima el resultado de la division de los mismos con una precision de dos decimales. Por ejemplo, si se ingresan los valores 4.5 y 7.2 debera imprimir: El resultado de dividir 4.5 por 7.2 es 0.62.
#############################################

num1 = float(input("Ingrese el primer numero real: "))
num2 = float(input("Ingrese el segundo numero real: "))
division = num1 / num2
print("El resultado de dividir ", num1, " por ", num2, " es ", round(division, 2))

##############################################
# Ejercicio 10 : Realizar un programa que permita al usuario ingrear una palabra y muestre en pantalla cuantos caracteres en total tiene la misma.
##############################################

palabra = input("Ingrese una palabra: ")
cantidad_caracteres = len(palabra)
print("La palabra ingresada tiene ", cantidad_caracteres, " caracteres en total.")

#####################################################################################################################################
# Estructura de decision simple

###############################################
# Ejercicio 12 : Implementar en Python el ejercicio anterior, es decir, leer dos numeros y determinar si son iguales, en caso afirmativo mostrar el mensaje “Son Iguales.”, en caso negativo mostrar el mensaje “No Son Iguales.”
###############################################

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 == num2:
    print("Son Iguales.")
else:
    print("No Son Iguales.")

################################################
# Ejercicio 13 : Leer dos numeros y determinar cual de ellos es el mayor, mostrando por pantalla "El valor mayor es:" y el correspondiente numero.
################################################

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print("El valor mayor es: ", num1)
else:
    print("El valor mayor es: ", num2)

###############################################
# Ejercicio 14 : Realice un programa que informe el valor total en pesos de una transaccion en dolares. Para ello, el programa debe leer el monto total en dolares de la transaccion, el valor del dolar al dıa de la fecha y el porcentaje (en pesos) de la comision que cobra el banco por la transaccion. Por ejemplo, si la transaccion se realiza por 10 dolares, el dolar tiene un valor 20,54 pesos y el banco cobra un 4 % de comision, entonces el programa debera informar: La transaccion sera de 213,61 pesos argentinos (resultado de multiplicar 10*20,54 y adicionarle el 4 %). 
###############################################

monto_dolares = float(input("Ingrese el monto total de la transaccion en dolares: "))
valor_dolar = 20.54
comision = 4
monto_pesos = monto_dolares * valor_dolar
monto_total = monto_pesos + (monto_pesos * comision / 100)
print("La transaccion sera de ", round(monto_total, 2), " pesos argentinos.")

###############################################
# Ejercicio 15 : Realizar un programa que lea 2 numeros enteros desde el teclado e informe en pantalla cual de los dos numeros es el mayor. Si son iguales debe informar en pantalla lo siguiente: "Los numeros ingresados son iguales". 
###############################################

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
if num1 > num2:
    print("El numero mayor es: ", num1)
elif num2 > num1:
    print("El numero mayor es: ", num2) 
else:
    print("Los numeros ingresados son iguales.")

#################################################
# Ejercicio 16 : Realizar un programa que lea un numero real e imprima su valor absoluto. El valor absoluto de un numero x, se escribe |x| y se define como: |x| = x cuando x ≥ 0 |x| = −x cuando x < 0.
#################################################

numero = float(input("Ingrese un numero real: "))
if numero >= 0:
    valor_absoluto = numero
else:
    valor_absoluto = -numero
print("El valor absoluto del numero ingresado es: ", valor_absoluto)

#################################################
# Ejercicio 17 : Realizar un programa que permita ingresar dos palabras, y determine si tienen la misma longitud o no. Mostrar un mensaje en pantalla en cada caso. Misma longitud, una menor, o una mayor.
#################################################

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
longitud_palabra1 = len(palabra1)
longitud_palabra2 = len(palabra2)
if longitud_palabra1 == longitud_palabra2:
    print("Las palabras ingresadas tienen la misma longitud.") 
elif longitud_palabra1 > longitud_palabra2:
    print("La primera palabra es mayor que la segunda.")
else:
    print("La segunda palabra es mayor que la primera.")

#################################################
# Ejercicio 18 : Realizar un programa que permita al usuario ingresar un numero y determine si es positivo o negativo.
#################################################

numero = float(input("Ingrese un numero: "))
if numero > 0:
    print("El numero ingresado es positivo.")
elif numero < 0:
    print("El numero ingresado es negativo.")
else:
    print("El numero ingresado es cero.")

#################################################
# Ejercicio 19 : Realizar un programa que permita al usuario ingresar dos numeros enteros, y ordenarlos de menor a mayor. Mostrarlos luego en pantalla.
#################################################

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
if num1 < num2:
    print("Los numeros ordenados de menor a mayor son: ", num1, " y ", num2)
elif num2 < num1:
    print("Los numeros ordenados de menor a mayor son: ", num2, " y ", num1)
else:
    print("Los numeros ingresados son iguales.")

################################################
# Ejercicio 20 : Simular la tirada de un dado, de 6 caras. Mostrar el resultado en pantalla. (debera utilizarla libreria random).
################################################

import random
dado = random.randint(1, 6) #Randint funcion de la libreria random y genera un numero entero al azar  dentro de un rango definido.
print("El resultado de la tirada del dado es: ", dado)

################################################
# Ejercicio 21 : Generar un valor entero al azar, entre 1 y 100. Determinar si el valor obtenido esta en la primera mitad de valores, es decir es menor o igual a 50, o no. 
################################################

import random
valor_azar = random.randint(1, 100)
if valor_azar <= 50:
    print("El valor obtenido es ", valor_azar, " y esta en la primera mitad de valores.")
else:
    print("El valor obtenido es ", valor_azar, " y esta en la segunda mitad de valores.")

################################################
# Ejercicio 22 :  Generar un valor aleatorio real, entre 0.0 y 1.0, sin incluir el 1.0 Determinar si el valor obtenido es menor a 0.5 o no. 
################################################

import random
valor_aleatorio = random.uniform(0.0, 1.0) #Uniform funcion de la libreria random y genera un numero con decimales al azar dentro de un rango definido.
if valor_aleatorio < 0.5:
    print("El valor obtenido es ", valor_aleatorio, " y es menor a 0.5.")
else:
    print("El valor obtenido es ", valor_aleatorio, " y no es menor a 0.5.")

################################################
# Ejercicio 23 : El usuario tendra un intento para ver si adivina que dado obtuvo la computadora. Esta simulara la tirada de un dado, y mantendra secreto su valor. El usuario ingresara el valor que cree la computadora obtuvo. Recibira un mensaje de felicitaciones si consigue adivinarlo, un mensaje de finalizacion del programa y de que ha perdido, en caso contrario.
################################################

import random
dado = random.randint(1, 6)
adivinanza = int(input("Adivina el valor del dado (entre 1 y 6): "))
if adivinanza == dado:
    print("Felicitaciones! Has adivinado el valor del dado.")
else:
    print("Game Over. El valor del dado era: ", dado)

#####################################################################################################################################
# Diseño de Algoritmos

################################################
# Ejercicio 25 : Implemente el algoritmo del punto anterior en Python, pidiendo un numero al usuario para determinar si es par o impar. 
################################################

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")