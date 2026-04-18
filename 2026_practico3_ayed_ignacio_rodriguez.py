# Intermedios y Avanzados

#########################################
# Ejercicio 1 : Concatenar dos listas en base a sus elementos y posiciones. Es decir, crear dos listas del mismo tamaño, y luego armar una tercer lista, a la cual primero se le agregue el primer elemento de la lista 1, luego el primer elemento de la lista 2. Luego se le agregue el segundo elemento de la lista 1, luego el segundo elemento de la lista 2, y asi suc. Ejemplo: Supongamos tenemos una lista de frutas y otra de verduras. La tercera quedara: ['damasco', 'frutilla', 'anana'] ['zanahoria', 'berenjena', tomate']
#########################################

frutas = ['damasco', 'frutilla', 'anana']
verduras = ['zanahoria', 'berenjena', 'tomate']

lista_concatenada = []
for i in range(len(frutas)):
    lista_concatenada.append(frutas[i])
    lista_concatenada.append(verduras[i])
print(lista_concatenada)

#########################################
# Ejercicio 2 : Suma de Numeros Positivos y Negativos: Se requiere un programa que permita el ingreso de 10 numeros y al finalizar muestre en pantalla la cantidad numeros positivos y por otra parte la cantidad de numeros negativos que fueron ingresados
#########################################

numeros = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
positivos = 0
negativos = 0
for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")

#########################################
# Ejercicio 3 : Dado un n ingresado por el usuario, realizar la suma de los n primeros terminos de la serie a continuacion. Mostrar el resultado. 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/n
#########################################

n = int(input("Ingrese un numero n: "))
suma = 0
for i in range(1, n + 1):
    suma += 1 / i
print(f"La suma de los {n} primeros terminos de la serie es: {suma}")

#########################################
# Ejercicio 4 : Se le permitira al usuario ingresar una frase. Se mostraran en pantalla solamente las letras en posiciones pares de la misma.
#########################################

frase = input("Ingrese una frase: ")
letras_pares = ""
for i in range(len(frase)):
    if i % 2 == 0:
        letras_pares += frase[i]
print(f"Las letras en posiciones pares son: {letras_pares}")

#########################################
# Ejercicio 5 : Diseñar un algoritmo en pseudocodigo que permita ingresar una frase al usuario y una letra, y determine cuantas veces esta esa letra en dicha frase. Luego que ya tenga el pseudocodigo, implementarlo en Python.
#########################################

"""ALGORITMO ContarCaracteres
    
 Declaracion de variables
    DEFINIR frase COMO Cadena
    DEFINIR letra COMO Caracter
    DEFINIR contador COMO Entero
    
Entrada de datos
    ESCRIBIR "Ingrese una frase: "
    LEER frase
    ESCRIBIR "Ingrese una letra: "
    LEER letra
    
Inicialización
    contador <- 0
    
Recorrido de la cadena
    PARA CADA char EN frase HACER
        SI char == letra ENTONCES
            contador <- contador + 1
        FIN SI
    FIN PARA
    
Salida de resultados
    ESCRIBIR "La letra '", letra, "' aparece ", contador, " veces en la frase."

FIN ALGORITMO"""

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra a investigar: ")
contador = 0
for char in frase:
    if char == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

#########################################
# Ejercicio 6 : Ingresar una frase que contenga sımbolos varios, ademas de mayusculas y minusculas mezclados. Determinar la cantidad de espacios, y cada sımbolo que hay en la misma. Definir un conjunto pequeno de sımbolos, por ejemplo numeral, asterisco, arroba y signos de admiracion.
#########################################

frase = input("Ingrese una frase: ")
simbolos = {'#': 0, '*': 0, '@': 0, '!': 0}
espacios = 0
for char in frase:
    if char == ' ':
        espacios += 1
    elif char in simbolos:
        simbolos[char] += 1
print(f"Cantidad de espacios: {espacios}")
for simbolo, cantidad in simbolos.items():
    print(f"Cantidad de '{simbolo}': {cantidad}")

#########################################
# Ejercicio 7 : Permita al usuario ingresar una frase. Cambie las letras a por 4 y las letras e por 3
#########################################

frase = input("Ingrese una frase: ")
frase_modificada = ""
for char in frase:
    if char == 'a' or char == 'A':
        frase_modificada += '4'
    elif char == 'e' or char == 'E':
        frase_modificada += '3'
    else:
        frase_modificada += char
print(f"Frase modificada: {frase_modificada}")

#########################################
# Ejercicio 8 : Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los espacios sean reemplazados por guion bajo y la extension por numerales. Piense en los nombres de archivo para generar un backup que utilizan muchos softwares para tener una copia de resguardo del documento en el cual se estaba trabajando por si ocurre por ejemplo, un corte de electricidad
#########################################

nombre_archivo = input("Ingrese el nombre del archivo: ")
nombre_modificado = nombre_archivo.replace(' ', '_').replace('.', '###')
print(f"Nombre modificado para backup: {nombre_modificado}")

#########################################
# Ejercicio 9 : Permitir ingresar al usuario un numero de un dıgito. Controlando se haya ingresado dicho numero de no mas de 1 dıgito de longitud, pasarlo a letras y mostrarlo en pantalla. (Ejemplo: Si ingresa 3, se vera como resultado ”tres”)
#########################################

digito = input("Ingrese un numero de un digito: ")
if len(digito) == 1 and digito.isdigit():
    numeros_letras = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve'
    }
    print(f"El numero {digito} se escribe como: {numeros_letras[digito]}")
else:
    print("Error: Debe ingresar un numero de un digito.")

#########################################
# Ejercicio 10 : Se le pedira al usuario una frase. Se mostraran en pantalla, una palabra por lınea de la misma. *no usar listas en este ejercicio
#########################################

frase = input("Ingrese una frase: ")
palabra = ""
for char in frase:
    if char != ' ':
        palabra += char
    else:
        if palabra:
            print(palabra)
            palabra = ""
if palabra:
    print(palabra)

#########################################
# Ejercicio 11 : Pedir el nombre al usuario, y corroborar si ese nombre existe entre los nombres de usuarios validos guardados en una lista.
#########################################

nombres_validos = ['Ignacio', 'Juan', 'Alejo', 'Agustin']
nombre_usuario = input("Ingrese su nombre: ")
if nombre_usuario in nombres_validos:
    print("Nombre valido. Bienvenido!")
else:
    print("Nombre no valido. Acceso denegado.")

#########################################
# Ejercicio 12 : Implemente un programa que pide al usuario 8 nombres. Su programa debe seleccionar los nombres que empiezan con la letra M
#########################################

nombres = []
for i in range(8):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
nombres_con_m = []
for nombre in nombres:
    if nombre.startswith('M') or nombre.startswith('m'):
        nombres_con_m.append(nombre)
print("Nombres que empiezan con M:")
for nombre in nombres_con_m:
    print(nombre)

#########################################
# Ejercicio 13 : Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra como elemento de una lista
#########################################

frase = input("Ingrese una frase: ")
letras = []
for char in frase:
    letras.append(char)
print("Lista de letras:")
for letra in letras:
    print(letra)

#########################################
# Ejercicio 14 : Realizar un programita que le pida ingresar una frase al usuario y coloque cada palabra de la misma como elemento de una lista. (¿Que nos permite distinguir una palabra de otra, en los caracteres?)
#########################################

frase = input("Ingrese una frase: ")
palabras = []
palabra = ""
for char in frase:
    if char != ' ':
        palabra += char
    else:
        if palabra:
            palabras.append(palabra)
            palabra = ""
if palabra:
    palabras.append(palabra)
print("Lista de palabras:")
for palabra in palabras:
    print(palabra)

#########################################
# Ejercicio 15 : El usuario debera poder ingresar varios nombres completos (ejemplo: ”Luis Perez”). El programa debera luego, colocar los nombres en una lista y los apellidos en otra
#########################################

nombres_completos = []
for i in range(5):
    nombre_completo = input("Ingrese un nombre completo (ejemplo: 'Luis Perez'): ")
    nombres_completos.append(nombre_completo)
nombres = []

apellidos = []
for nombre_completo in nombres_completos:
    partes = nombre_completo.split()
    if len(partes) >= 2:
        nombres.append(partes[0])
        apellidos.append(partes[1])
print("Nombres:")
for nombre in nombres:
    print(nombre)
print("Apellidos:")
for apellido in apellidos:
    print(apellido)
    
#########################################
# Ejercicio 16 : Dada una lista de numeros, ingresada por el usuario o inventada por usted, cree otra lista con la cantidad de dıgitos de cada numero de la misma.
#########################################

numeros = []
for i in range(5):
    numero = input("Ingrese un numero: ")
    numeros.append(numero)
cantidad_digitos = []
for numero in numeros:
    cantidad_digitos.append(len(numero))
print("Cantidad de digitos de cada numero:")
for i in range(len(numeros)):
    print(f"Numero: {numeros[i]}, Cantidad de digitos: {cantidad_digitos[i]}")


#########################################
# Ejercicio 17 : Numero Invertido: Se requiere mostrar en pantalla un numero invertido de 6 cifras, al que fuera ingresado por teclado. (Ejemplo: en pantalla se vera: “El numero ingresado es 140975, invertido es: 579041”)
#########################################

numero = input("Ingrese un numero de 6 cifras: ")
if len(numero) == 6 and numero.isdigit():
    numero_invertido = numero[::-1]
    print(f"El numero ingresado es {numero}, invertido es: {numero_invertido}")
else:
    print("Error: Debe ingresar un numero de 6 cifras.")

#########################################
# Ejercicio 18 : El usuario debera ingresar la longitud de la base de una piramdide y el algoritmo debera imprimir en pantalla una piramide de numerales. (Ejemplo: Si el usuario ingresa 7, se vera en pantalla: Determine que restricciones deberia contemplar para que el triangulo quede bien formado. Cualquier valor para la longitud de la base servira?
#########################################

base = int(input("Ingrese la longitud de la base de la piramide (debe ser un numero impar): "))
if base % 2 == 1 and base > 0:
    altura = (base + 1) // 2
    for i in range(altura):
        espacios = ' ' * (altura - i - 1)
        piramide = '#' * (2 * i + 1)
        print(espacios + piramide + espacios)
else:
    print("Error: La longitud de la base debe ser un numero impar y mayor que 0.")

#Se tiene que ingresar un numero impar para que la piramide quede bien formada, ya que si se ingresa un numero par no se podra centrar el simbolo de la punta de la piramide

###########################################################################################################################

# Avanzados

#########################################
# Ejercicio 19 : Simulador de Quini 6: Se requiere un programa que genere una lista de 6 numeros aleatorios entre 0 y 45. Asegurese de que ningun numero se repita en la lista. Al finalizar, muestre los numeros ordenados de menor a mayor. (Pista: Debera controlar la existencia del numero antes de agregarlo). Si podra usar el comando sort o sorted de las listas, investigue las diferencias, y decida cual usar, escribar su justificacion como un comentario en el codigo para ordenarla.
#########################################

import random

numeros_quini6 = []
while len(numeros_quini6) < 6:
    numero = random.randint(0, 45)
    if numero not in numeros_quini6:
        numeros_quini6.append(numero)
numeros_quini6.sort()  #Uso sort porque modifica la lista original y no necesito conservar el orden original de los numeros generados
print("Numeros del Quini 6 ordenados de menor a mayor:")
for numero in numeros_quini6:
    print(numero)

#########################################
# Ejercicio 20 : Comprension basica de cadenas: El usuario debera ingresar una frase que contenga letras repetidas ("aaabbccccd"). El programa debera generar una nueva cadena que resuma el contenido indicando la letra y su cantidad (a3b2c4d1)
#########################################

frase = input("Ingrese una frase con letras repetidas: ")
resumen = ""
i = 0
while i < len(frase):
    letra = frase[i]
    contador = 1
    while i + 1 < len(frase) and frase[i + 1] == letra:
        contador += 1
        i += 1
    resumen += letra + str(contador)
    i += 1
print(f"Resumen de la frase: {resumen}")

#########################################
# Ejercicio 21 : Cifrado Cesar: Diseñe un programa que permita ingresar una frase y un numero de desplazamiento n. El algoritmo debe mostrar la frase cifrada reemplazando cada letra por la que se encuentra n posiciones mas adelante en el abecedario.
#########################################

frase = input("Ingrese una frase: ")
desplazamiento = int(input("Ingrese el numero de desplazamiento: "))
frase_cifrada = ""
for char in frase:
    if char.isalpha(): #Uso isalpha para verificar si el caracter es una letra de esta manera se ignoran los espacios y simbolos
        base = ord('A') if char.isupper() else ord('a')
        letra_cifrada = chr((ord(char) - base + desplazamiento) % 26 + base)
        frase_cifrada += letra_cifrada
    else:
        frase_cifrada += char
print(f"Frase cifrada: {frase_cifrada}")

#########################################
# Ejercicio 22 : Analisis de notas de Examen: Un profesor necesita procesar las notas de una comision. Permita ingresar una lista de 10 notas (floats). El programa debe determinar el promedio general, la nota mas alta y la mas baja, cuantos alumnos aprobaron con nota mayor o igual a 6 y cuantos promocionaron con nota mayor o igual a 8
#########################################

notas = []
for i in range(10):
    nota = float(input("Ingrese una nota (0-10): "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
alumnos_aprobados = sum(1 for nota in notas if nota >= 6)
alumnos_promocionados = sum(1 for nota in notas if nota >= 8)
print(f"Promedio general: {promedio:.2f}")
print(f"Nota mas alta: {nota_mas_alta}")
print(f"Nota mas baja: {nota_mas_baja}")
print(f"Cantidad de alumnos aprobados con nota mayor o igual que 6: {alumnos_aprobados}")
print(f"Cantidad de alumnos promocionados con nota mayor o igual que 8: {alumnos_promocionados}")

#########################################
# Ejercicio 23 : Buscador de Subcadenas (Manual): Pida al usuario que ingrese una frase y una palabra corta. Sin utilizar el operador in ni el metodo .find(), determine mendiante bucles si la palabra se ecuentra dentro de la frase y en que posicion comienza.
#########################################

frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra corta a buscar: ")
encontrada = False
for i in range(len(frase) - len(palabra) + 1):
    if frase[i:i+len(palabra)] == palabra:
        print(f"La palabra '{palabra}' se encuentra en la frase, comenzando en la posicion {i}.")
        encontrada = True
        break
if not encontrada:
    print(f"La palabra '{palabra}' no se encuentra en la frase.")

#########################################
# Ejercicio 24 : Filtro de elementos unicos: Dada una lista de numeros ingresada por el usuario (que puede contener duplicados), cree una segunda lista que contenga los mismos elementos pero sin ninguna repeticion. Muestre ambas listas para comparar. No puede utilizar conjuntos (set) para resolverlo.
#########################################

numeros = []
for i in range(10):
    numero = int(input("Ingrese un numero:"))
    numeros.append(numero)
numeros_unicos = []
for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)
print("Lista original con posibles duplicados:")
print(numeros)
print("Lista de numeros unicos sin duplicados:")
print(numeros_unicos)

#########################################
# Ejercicio 25 : Suma de Matriz 3x3: Simule una matriz de 3x3 utilizando listas anidada (una lista que contiene 3 listas de 3 elementos cada una). El usuario debera cargar los 9 numeros. Luego, el programa debe mostrar la matriz en formato de tabala y calcular la suma de los elementos de la diagonal principal. 
#########################################

matriz = []
print("Ingrese los numeros para la matriz 3x3:")
for i in range(3):
    fila = []
    for n in range(3):
        numero = int(input(f"Ingrese el numero para la posicion [{i}][{n}]: "))
        fila.append(numero)
    matriz.append(fila)
print("Matriz 3x3:")
for fila in matriz:
    print("\t".join(str(num) for num in fila))
suma_diagonal = matriz[0][0] + matriz[1][1] + matriz[2][2]
print(f"Suma de los elementos de la diagonal principal: {suma_diagonal}")

#########################################
# Ejercicio 26 : Validador de contraseñas seguras: El usuario debe ingresar una propuesta de contraseña. El programa debe informar si es segura o insegura, basandonse en: debe tener al menos 8 caracteres y debe contener al menos un numero, una mayuscula y un simbolo de los definidos en el ejercicio 6
#########################################

contraseña = input("Ingrese una contraseña: ")
simbolos_validos = {'#', '*', '@', '!'}
es_segura = True
if len(contraseña) < 8:
    es_segura = False
if not any(char.isdigit() for char in contraseña):
    es_segura = False
if not any(char.isupper() for char in contraseña):
    es_segura = False
if not any(char in simbolos_validos for char in contraseña):
    es_segura = False
if es_segura:
    print("La contraseña es segura.")
else:
    print("La contraseña es insegura. Debe tener al menos 8 caracteres, contener al menos un numero, una mayuscula y un simbolo de los siguientes: #, *, @, !")

#########################################
# Ejercicio 27 : Histograma de palabras: Pida una frase al usuario y coloque cada palabra en una lista, sin utilizar split o list, reaclice el proceso de modo artesanal. Luego para cada palabra, muestre en pantalla su nombre seguido de tantos astericos como letras tenga. Ejemplo: Hola sol -> Hola ****, sol ***
#########################################

frase = input("Ingrese una frase: ")
palabras = []
palabra = ""
for char in frase:
    if char != ' ':
        palabra += char
    else:
        if palabra:
            palabras.append(palabra)
            palabra = ""
if palabra:
    palabras.append(palabra)
print("Histograma de palabras:")
for palabra in palabras:
    print(f"{palabra} {'*' * len(palabra)}")

#########################################
# Ejercicio 28 : Interseccion de Listas: Cree dos listas de 5 nombres cada una (ingresadas por el usuario). El programa debe generar una tercera lista que contenga unicamente los nombres que aparecen en ambas listas originales. Si no hay concidencias, informar al usuario.
#########################################

lista1 = []
lista2 = []
print("Ingrese 5 nombres para la primera lista:")
for i in range(5):
    nombre = input(f"Nombre {i + 1}: ")
    lista1.append(nombre)

print("Ingrese 5 nombres para la segunda lista:")
for i in range(5):
    nombre = input(f"Nombre {i + 1}: ")
    lista2.append(nombre)
interseccion = []
for nombre in lista1:
    if nombre in lista2 and nombre not in interseccion:
        interseccion.append(nombre)
if interseccion:
    print("Nombres que aparecen en ambas listas:")
    for nombre in interseccion:
        print(nombre)
else:
    print("No hay nombres que aparezcan en ambas listas.")

#########################################
# Ejercicio 29 : La gran X: Pida un numero impar (validar que sea impar). El programa debe dibujar una letra X gigante que cruce un cuadrado de ese tamaño utilizando un caracte a eleccion.
#########################################

tamaño = int(input("Ingrese un numero impar para el tamaño de la X: "))
if tamaño % 2 == 1 and tamaño > 0:
    for i in range(tamaño):
        linea = ""
        for j in range(tamaño):
            if j == i or j == tamaño - i - 1:
                linea += 'X'
            else:
                linea += ' '
        print(linea)
else:
    print("Error: El numero debe ser impar y mayor que 0.")