# Recursion

#########################################
# Ejercicio 1 : Implementar la funcion factorial de un numero de modo recursivo y mostrarlo en pantalla
#########################################
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


#########################################
# Ejercicio 2 : Implementar una funcion recursiva que tome un parametro numerico n y devuelva la suma desde 1 hasta n y mostrarlo en pantalla
#########################################
def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n - 1)

#########################################
# Ejercicio 3 : Implementar una funcion recursiva llamada potencia que tome dos parametros numericos, una base b y una potencia p y devuelva b^p
#########################################
def potencia(b, p):
    if p == 0:
        return 1
    else:
        return b * potencia(b, p - 1)

#########################################
# Ejercicio 4 : Implementar de modo recursivo, la funcion de Fibonacci, donde f0 = 0, f1 = 1 y fn = fn-1 + fn-2
#########################################
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#########################################
# Ejercicio 5 : Implementar una funcion recursiva que tome una lista como parametro y devuelva la suma de todos sus elementos 
#########################################
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])
        
#########################################
# Ejercicio 6 : Implementar una funcion recursiva llamada invertir que tome una frase como parametro y la devuelva invertida
#########################################
def invertir(frase):
    if len(frase) == 0:
        return ""
    else:
        return frase[-1] + invertir(frase[:-1])

#########################################
# Ejercicio 7 : Implementar una funcion recursiva que tome como parametro una lista de nombres y una letra, y que devuelva la cantidad de nombres que empiezan con dicha letra
#########################################
def contar_nombres(lista, letra):
    if len(lista) == 0:
        return 0
    else:
        if lista[0].startswith(letra):
            return 1 + contar_nombres(lista[1:], letra)
        else:
            return contar_nombres(lista[1:], letra)

#########################################
# Ejercicio 8 : Implementar uan funcion recursiva llamada pares que tome una lista de numeros como parametro y devuelva una lista de valores logicos donde true signifca ese numero es par en la lista y false que no lo es
#########################################
def pares(lista):
    if len(lista) == 0:
        return []
    else:
        es_par = lista[0] % 2 == 0
        return [es_par] + pares(lista[1:])
        
#########################################
# Ejercicio 9 : Implementar una funcion recursiva que tome como parametro una lista de numeros enteros y determine la cantidad de numeros 1 que hay en la misma
#########################################
def contar_unos(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] == 1:
            return 1 + contar_unos(lista[1:])
        else:
            return contar_unos(lista[1:])

#########################################
# Ejercicio 10 : Implementar una funcion recursiva que tome como parametro una lista de marcas de vehiculo y determine cuantos hay de la marca Kawasaki
#########################################
def contar_kawasaki(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0].lower() == "kawasaki":
            return 1 + contar_kawasaki(lista[1:])
        else:
            return contar_kawasaki(lista[1:])

#########################################
# Ejercicio 11 : Implementar una funcion recurisva que dada una lista de nombres determine cuantos empiezan con la letra M
#########################################
def contar_m(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0].lower().startswith("m"):
            return 1 + contar_m(lista[1:])
        else:
            return contar_m(lista[1:])

#########################################
# Ejercicio 12 : Implementar una funcion recursiva que tome una palabra y determina la cantidad de vocales que tiene
#########################################
def contar_vocales(palabra):
    if len(palabra) == 0:
        return 0
    else:
        if palabra[0].lower() in "aeiou":
            return 1 + contar_vocales(palabra[1:])
        else:
            return contar_vocales(palabra[1:])

#########################################
# Ejercicio 13 : Implementar una funcion recursiva llamada max que tome una lista como parametro y devuelva el valor maximo de la lista
#########################################
def max(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_restante = max(lista[1:])
        return lista[0] if lista[0] > max_restante else max_restante

#########################################
# Ejercicio 14 : Implementar una funcion recursiva llamada min que tome una lista como parametro y devuelva el valor minimo de la lista
#########################################
def min(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        min_restante = min(lista[1:])
        return lista[0] if lista[0] < min_restante else min_restante

#########################################
# Ejercicio 15 : Implementar una funcion recursiva que tome una cadena de caracteres y la devuelva invertida
#########################################
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

#########################################
# Ejercicio 16 : Implementar una funcion recursiva que calcule el maximo comun divisor de dos numeros a y b
#########################################
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

#########################################
# Ejercicio 17 : Utilizar una funcion recursiva para diseñar que determine si una cadena de caracteres tiene mas vocales que consonantes
#########################################
def mas_vocales(cadena):
    if len(cadena) == 0:
        return 0, 0
    else:
        vocales, consonantes = mas_vocales(cadena[1:])
        if cadena[0].lower() in "aeiou":
            return vocales + 1, consonantes
        elif cadena[0].isalpha():
            return vocales, consonantes + 1
        else:
            return vocales, consonantes

#########################################
# Ejercicio 18 : Implementar una funcion recursiva que reacomode una lista de numeros enteros de modo tal que todos los valores pares queden primero que todos los valores impares
#########################################
def reacomodar_pares_impares(lista):
    if len(lista) == 0:
        return []
    else:
        pares = reacomodar_pares_impares([x for x in lista[1:] if x % 2 == 0])
        impares = reacomodar_pares_impares([x for x in lista[1:] if x % 2 != 0])
        if lista[0] % 2 == 0:
            return [lista[0]] + pares + impares
        else:
            return pares + [lista[0]] + impares

            