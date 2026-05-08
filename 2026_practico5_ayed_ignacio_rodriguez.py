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

