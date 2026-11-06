# Notacion Big O

#########################################
# Ejercicio 1: Dado el siguiente código, determine cuál es su Big O[cite: 1].
#########################################
x = 3 * 230 + 2 * (-3)

# RESOLUCIÓN:
# Es O(1). 
# Justificación: La máquina solo hace un cálculo matemático simple y lo guarda 
# en la variable 'x'[cite: 1]. Tarda exactamente lo mismo siempre, porque no hay 
# listas ni ciclos que la hagan trabajar de más.

#########################################
# Ejercicio 2: Dado el siguiente código, determine cuál es su Big O[cite: 1].
#########################################
x = 5 * 3 - 21
y = 3 * 2
print (x + y)

# RESOLUCIÓN:
# Es O(1). 
# Justificación: Igual que el anterior. Son tres renglones de código fijo[cite: 1]. 
# Como no depende de la cantidad de datos que le ingreses, el tiempo que tarda 
# es constante.

#########################################
# Ejercicio 3: Se tiene una función que determina si un número es par o no. ¿Cuál es su Big O?[cite: 1]
#########################################
def es_par(n):
    if (n % 2 == 0):
        return True
    else:
        return False

# RESOLUCIÓN:
# Es O(1). 
# Justificación: Solamente agarra el número 'n', lo divide por 2 para ver el resto, 
# y te avisa si es verdadero o falso[cite: 1]. No importa si 'n' vale 2 o si vale 
# 10 millones, le toma el mismo esfuerzo hacer esa única comprobación.

#########################################
# Ejercicio 4: Dado el siguiente código, determine cuál es su Big O[cite: 2].
#########################################
n = int(input("Ingrese un numero n:"))
for x in range(n):
    print(x)

# RESOLUCIÓN:
# Es O(n). 
# Justificación: Acá entra el ciclo 'for'. El código va a dar tantas vueltas y va 
# a imprimir tantas veces como indique el número 'n'[cite: 2]. El tiempo de 
# ejecución crece linealmente a la par del tamaño de 'n'.

#########################################
# Ejercicio 5: Suponiendo que en sus bloques de código internos tiene los Big O descriptos. Determine cuál es el Big O del algoritmo total[cite: 2].
#########################################
# if x == 0:
#     # O(1)
# elif x < 0:
#     # O(log(n))
# else:
#     # O(n**2)

# RESOLUCIÓN:
# Es O(n^2). 
# Justificación: Big O siempre te pide que te pongas en el peor escenario posible. 
# Aunque los dos primeros 'if' son rápidos, si el código cae en el 'else', 
# va a tardar O(n^2)[cite: 2]. Esa es la parte más pesada y es la que "gana" al clasificarlo.

#########################################
# Ejercicio 6: Dado el siguiente código, determine cuál es su Big O[cite: 2].
#########################################
def imprimir_doble(palabra):
    for letra in palabra:
        print (letra)
    for letra in palabra:
        print (letra)

# RESOLUCIÓN:
# Es O(n). 
# Justificación: Tenés un bucle que recorre la palabra, y cuando termina, 
# arranca otro bucle igual[cite: 2]. Técnicamente sería O(n) + O(n) = O(2n). 
# Pero en esta notación matemática los números fijos (constantes) se ignoran, 
# así que queda simplemente O(n).

#########################################
# Ejercicio 7: Algoritmo que devuelve el índice de la primer ocurrencia en el vector del número n. Determinar su Big O[cite: 2].
#########################################
def indice_primera_ocurrencia(n, vector):
    for i in range (len (vector)):
        if vector[i] == n:
            return i
    return -1

# RESOLUCIÓN:
# Es O(n). 
# Justificación: Capaz tenés suerte y encontrás el número en el primer lugar del vector. 
# Pero pensando en el "peor caso", el número podría no estar, obligando al ciclo 'for' 
# a revisar cada uno de los elementos de principio a fin[cite: 2].

#########################################
# Ejercicio 8: Se requiere que la función devuelva todos los indices donde se encuentra el número n. Determinar su Big O[cite: 2].
#########################################
def ocurrencias(n, vector):
    indices = []
    for i in range (len (vector)):
        if vector[i] == n:
            indices.append(i)
    return indices

# RESOLUCIÓN:
# Es O(n). 
# Justificación: Sí o sí tiene que recorrer todo el vector completo una sola vez 
# para ir guardando los lugares donde aparece el número 'n'[cite: 2]. Por eso el 
# esfuerzo es proporcional al tamaño del vector.

#########################################
# Ejercicio 9: Procedimiento que toma una lista, imprime todos los números y luego la suma de a pares. Determine su Big O[cite: 3].
#########################################
def sumas(nros):
    print('Estos son todos los numeros que hay:')
    for n in nros:
        print (n)
    print('Estas son las sumas de a pares:')
    for primero in nros:
        for segundo in nros:
            print (primero + segundo)

# RESOLUCIÓN:
# Es O(n^2). 
# Justificación: El primer 'for' es O(n) porque recorre la lista una vez. Pero después, 
# tenés un 'for' metido adentro de otro 'for', lo que hace que recorra la lista 
# multiplicando las vueltas (n * n)[cite: 3]. Eso nos da O(n^2). Al final queda O(n) + O(n^2), 
# y siempre manda el término más grande.