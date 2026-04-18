# Introduccion a secuencias ordenadas en Python (strings, listas)

#########################################
# Ejercicio 1 : Guarde en una variable, la palabra ’Mordor’. Muestre en pantalla las letras en las posiciones 1 y 3. ¿Que letras resultan ser?
#########################################

palabra = 'Mordor'
print(palabra[1]) # o
print(palabra[3]) # d
# Python empieza a contar desde 0

#########################################
# Ejercicio 2 : Pida una frase al usuario. Muestre su primer letra en pantalla. Muestrela en mayusculas tambien.
#########################################

frase = input('Ingrese una frase: ')
print(frase[0]) 
print(frase[0].upper()) 

#########################################
# Ejercicio 3 : Pida una frase al usuario, controle que tenga una longitud total mayor a 5 caracteres.Muestre en pantalla los primeros 3 caracteres de la misma.
#########################################

frase = input('Ingrese una frase: ')
if len(frase) > 5:
    print(frase[:3]) 
else:
    print('La frase debe tener mas de 5 caracteres')

#########################################
# Ejercicio 4 : Dada la siguiente lista de compras de ingredientes para preparar una torta, mostrarla en pantalla, un ingrediente por lınea. Luego corregir el ultimo a ”Canela en polvo” [”Chocolate”, ”Huevos”, ”Manteca”, ”Crema de leche”, ”Frutillas”]
#########################################

ingredientes = ["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutillas"]
for ingrediente in ingredientes:
    print(ingrediente)
ingredientes[-1] = "Canela en polvo"
print(ingredientes)

#########################################
# Ejercicio 5 : Pida un numero al usuario, mayor que 1 y menor a 50. Muestre en pantalla los nuumeros de 1 hasta ese nuumero ingresado, uno por lınea.
#########################################

numero = int(input('Ingrese un numero entre 1 y 50: '))
if numero > 1 and numero < 50:
    for i in range(1, numero + 1):
        print(i)
else:
    print('El numero debe ser mayor que 1 y menor que 50')

#########################################
# Ejercicio 6 : Dada la siguiente lista de valores numericos [2, 65, 34, 3, 8, 65] Realice la suma de los elementos que estan ubicados en las posiciones 0, 2 y 5 Muestre el resultado en pantalla.
#########################################

numeros = [2, 65, 34, 3, 8, 65]
suma = numeros[0] + numeros[2] + numeros[5]
print(suma)

#########################################
# Ejercicio 7 : Dada la siguiente lista de valores numericos [56, 7, 34, 19, 3, 1, 76, 2, 81, 4, 2, 8] muestre enpantalla solo los elementos de la misma que estan ubicados en posiciones pares, como 0,2, 4, etc (¿Como puede determinar si un nro es par o no? ¿Debera escribir cada print dea uno, o debera considerar realizar un recorrido por la lista, usando un bucle?)
#########################################

numeros = [56, 7, 34, 19, 3, 1, 76, 2, 81, 4, 2, 8]
for i in range(len(numeros)):
    if i % 2 == 0: 
        print(numeros[i])

#########################################
# Ejercicio 8 : * Pedir dos palabras, por separado, al usuario y mostrarlas en pantalla concatenadas, es decir, una seguida de la otra. ¿Cuales son todas las maneras en que se pueden mostrar concatenadas en pantalla, cadenas de caracteres? ¿Que diferencia hay entre mostrarlas una seguida de otra en pantalla, y en concatenarlas?
#########################################

palabra1 = input('Ingrese la primera palabra: ')
palabra2 = input('Ingrese la segunda palabra: ')
concatenada = palabra1 + palabra2
print(concatenada)
print(palabra1, palabra2)
# La diferencia entre mostrar las palabras concatenadas y mostrarlas una seguida de la otra es que en la primera se crea una nueva cadena de caracteres que contiene ambas palabras, mientras que en la segunda se muestran las palabras por separado pero en la misma linea.

#########################################
# Ejercicio 9 : * Guarde en dos variables de listas diferentes los siguientes elementos: [“amarillo“, “azul“,“violeta“] y [“zapallo“, “tomate“, “limon“] Genere una nueva lista que sea la concatenacion de ambas, le debera quedar [“amarillo“, “azul“, “violeta“, “zapallo“, “tomate“, “limon“]
#########################################

colores = ["amarillo", "azul", "violeta"]
verduras = ["zapallo", "tomate", "limon"]
concatenada = colores + verduras
print(concatenada)

#########################################
# Ejercicio 10 : * Pedir una palabra al usuario. Mostrar en pantalla una nueva palabra que este formada por la primera letra, la letra del medio y la ultima letra. Por ejemplo, si se ingreso “patos“ se vera “pts“ y si se ingresa “zapato“ se vera “zao“.
#########################################

palabra = input('Ingrese una palabra: ')
primera_letra = palabra[0]
letra_medio = palabra[len(palabra) // 2]
ultima_letra = palabra[-1]
nueva_palabra = primera_letra + letra_medio + ultima_letra
print(nueva_palabra)

#########################################
# Ejercicio 11 :  * Pedir una palabra al usuario y armar una nueva palabra que sea los tres caracteres del medio de la palabra ingresada. 
#########################################

palabra = input('Ingrese una palabra: ')
if len(palabra) >= 3:
    medio = len(palabra) // 2
    nueva_palabra = palabra[medio - 1:medio + 2]
    print(nueva_palabra)
else:
    print('La palabra debe tener al menos 3 caracteres')

#########################################
# Ejercicio 12 : El usuario podra ingresar nombre y apellido. El programa debera convertir las iniciales en mayusculas y las demas letras en minusculas.
#########################################

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
nombre_mayuscula = nombre.capitalize()
apellido_mayuscula = apellido.capitalize()
print(nombre_mayuscula, apellido_mayuscula)

###########################################################################################################################

# Introduccion al Bucle For

#########################################
# Ejercicio 13 : Imprimir en pantalla, la palabra "hobbit" 20 veces.
#########################################

for i in range(20):
    print("hobbit")

#########################################
# Ejercicio 14 : Imprimir en pantalla, los numeros del 1 al 10. Luego del 1 al 100. ¿Que modifico para la primer tanda de valores, respecto a la segunda tanda de valores?
#########################################

for i in range(1, 11):
    print(i)
for i in range(1, 101):
    print(i)

#########################################
# Ejercicio 15 : Pida 10 nombres de pelıculas al usuario. Guardelos en una lista. Luego pida al usuario que ingrese un numero n del 1 al 10. Controle que n este en el rango correcto, es decir entre 1 y 10. Muestre en pantalla cual es la pelıcula n-esima. Por ejemplo, si el usuario me ingresa 1, debo mostrar la primer pelıcula de la lista.
#########################################

peliculas = []
for i in range(10):
    pelicula = input('Ingrese el nombre de una película: ')
    peliculas.append(pelicula)
n = int(input('Ingrese un numero del 1 al 10: '))
if n >= 1 and n <= 10:
    print(peliculas[n - 1])
else:
    print('El numero debe estar entre 1 y 10')

#########################################
# Ejercicio 16 : Se deberan ingresar 8 notas. Se mostrara el promedio, redondeado a 2 decimales.
#########################################
notas = []
for i in range(8):
    nota = float(input('Ingrese una nota: '))
    notas.append(nota)
promedio = sum(notas) / len(notas)
print(f'El promedio es: {promedio:.2f}') #:.2f redondea el promedio a 2 decimales

#########################################
# Ejercicio 17 : Pedir al usuario una frase. Determinar de al menos dos modos diferentes (con y sin listas) la cantidad de palabras que hay en dicha frase
#########################################

frase = input('Ingrese una frase: ')

# Metodo 1: Sin listas
contador = 1
for caracter in frase:
    if caracter == ' ':
        contador += 1
print(f'La cantidad de palabras es: {contador}')

# Metodo 2: Con listas
palabras = frase.split() #split() divide la frase en palabras y las guarda en una lista
cantidad_palabras = len(palabras)
print(f'La cantidad de palabras es: {cantidad_palabras}')

#########################################
# Ejercicio 18 : Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada nota, y guardarlas.
#########################################

cantidad_notas = int(input('Ingrese la cantidad de notas que desea ingresar: '))
notas = []
for i in range(cantidad_notas):
    nota = float(input('Ingrese una nota: '))
    notas.append(nota)
print('Las notas ingresadas son:', notas)

###########################################################################################################################

# Pseudo Aleatoriedad

#########################################
# Ejercicio 19 : Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas. (cuando se mencione un ’dado’, se considera que representa un valor al azar)
#########################################

import random

tiradas = []
for i in range(20):
    tirada = random.randint(1, 6) 
    tiradas.append(tirada)
promedio = sum(tiradas) / len(tiradas)
print('Las tiradas fueron:', tiradas)
print(f'El promedio de las tiradas es: {promedio:.2f}')

#########################################
# Ejercicio 20 : Tirar ahora, 2500 veces un dado de 6 caras. Mostrar el promedio de esas tiradas. Comparar con el promedio del ejercicio anterior. ¿Nota una diferencia sustancial habiendo cambiado la cantidad de tiradas?
#########################################

import random

tiradas = []
for i in range(2500):
    tirada = random.randint(1, 6) 
    tiradas.append(tirada)
promedio = sum(tiradas) / len(tiradas)
print(f'El promedio de las tiradas es: {promedio:.2f}')
# La diferencia es que al aumentar la cantidad de tiradas, el promedio puede acercarse mas al valor esperado que es 3.5 para un dado de 6 caras, mientras que con 20 tiradas el promedio puede ser mas variable. 

#########################################
# Ejercicio 21 : Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de la lista.
#########################################

import random

marcas = []
for i in range(10):
    marca = input('Ingrese una marca favorita: ')
    marcas.append(marca)
marca_aleatoria = random.choice(marcas) # choice() selecciona un elemento al azar de la lista
print('Una marca al azar de la lista es:', marca_aleatoria)

#########################################
# Ejercicio 22 : Llenar una lista de 20 elementos, con valores numericos enteros aleatrorios entre 1 y 50.
#########################################

import random

numeros = []
for i in range(20):
    numero = random.randint(1, 50) 
    numeros.append(numero)
print('La lista de numeros aleatorios es:', numeros)

#########################################
# Ejercicio 23 : Llenar una lista con 100 valores numericos reales aleatorios en el rango [0.0, 2.5]
#########################################

import random

numeros = []
for i in range(100):
    numero = random.uniform(0.0, 2.5) # uniform() genera un numero real aleatorio entre los limites especificados
    numeros.append(numero)
print('La lista de numeros aleatorios es:', numeros)


#########################################
# Ejercicio 24 : Dada una lista de colores, en base a la cantidad de elementos que la lista contenga, generar una posicion al azar v´alida, y mostrar el elemento en dicha posicion. Dicho de modo coloquial, elegir un elemento al azar de dicha lista. Realizar una primer version sin utilizar el comando choice de la librerıa random. Generar luego, una segunda version utilizando dicho comando. [’fthalo_blue’, ’medium_red’, ’payne_grey’, ’cobalt_blue’]
#########################################

import random

colores = ['fthalo_blue', 'medium_red', 'payne_grey', 'cobalt_blue']

# Version sin choice
posicion_aleatoria = random.randint(0, len(colores) - 1)
color_aleatorio = colores[posicion_aleatoria]
print('El color aleatorio es:', color_aleatorio)

# Version con choice
color_aleatorio = random.choice(colores)
print('El color aleatorio es:', color_aleatorio)

###########################################################################################################################

# Introduccion a Graficas en Python con la libreria Matplotlib

#########################################
#Ejercicio 25 : Para x desde 0 hasta 1000, graficar la funcion f(x) = 2x
#########################################

import matplotlib.pyplot as plt

x = list(range(1001))
f_x = [2 * i for i in x]
plt.plot(x, f_x)
plt.title('Grafica de f(x) = 2x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

#########################################
# Ejercicio 26 : Para unos 50 valores x entre 0 y 30, equidistantes, graficar la funcion f(x) = cos(x)
#########################################

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 30, 50)
f_x = np.cos(x)
plt.plot(x, f_x)
plt.title('Grafica de f(x) = cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

#########################################
# Ejercicio 27 : Crear dos vectores x e y, con 200 valores aleatorios. Generar una grafica del tipo scatter. (Investigar en la documentacion oficial Matplotlib scatter - Doc )
#########################################

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(200) #200 valores aleatorios entre 0 y 1
y = np.random.rand(200) #00 valores aleatorios entre 0 y
plt.scatter(x, y)
plt.title('Grafica de tipo scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#########################################
# Ejercicio 28 : Crear una grafica tipo scatter comparando la relacion entre alturas y pesos, de tres grupos de personas, listados a continuacion: pesos1 = [67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56] alturas1 = [101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 125.3, 114.9] pesos2 = [61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6] alturas2 = [152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1] pesos3 = [68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7] alturas3 = [165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 235.1, 181.1, 177.3]
#########################################

import matplotlib.pyplot as plt

pesos1 = [67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56]
alturas1 = [101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 125.3, 114.9]
pesos2 = [61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6]
alturas2 = [152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1]
pesos3 = [68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7]
alturas3 = [165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 235.1, 181.1, 177.3]

plt.scatter(alturas1, pesos1, label='Grupo 1')
plt.scatter(alturas2, pesos2, label='Grupo 2')
plt.scatter(alturas3, pesos3, label='Grupo 3')
plt.title('Relación entre alturas y pesos')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.grid()
plt.show()


