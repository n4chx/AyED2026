# Arreglos implementados con listas
# Para los siguientes ejercicios, podras utilizar las listas, que si bien no son arreglos, pueden simular serlo, en vez de utilizar numpy arrays

#########################################
# Ejercicio 1 : Diseñar un algoritmo que recorra las butacas de una sala de cine y determine cuantas butacas desocupadas hay en la sala, supongo que inicialmente tiene un array con valores booleanos, donde si es True implica que esta ocupada y si es False, la butaca esta desocupada
#########################################
def contar_butacas_desocupadas(butacas):
    contador_desocupadas = 0
    for butaca in butacas:
        if not butaca:  
            contador_desocupadas += 1
    return contador_desocupadas

#########################################
# Ejercicio 2 : Ingresar 10 numeros por teclado en dos arreglos alternadamente, un valor para uno el otro valor para el otro, y asi sucesivamente, luego mostrar el primer arreglo y en la siguiente linea mostrar el segundo arreglo
#########################################
def ingresar_numeros_alternados():
    arreglo1 = []
    arreglo2 = []
    
    for i in range(10):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        if i % 2 == 0:  
            arreglo1.append(numero)
        else:  
            arreglo2.append(numero)
    
    print("Primer arreglo:", arreglo1)
    print("Segundo arreglo:", arreglo2)

#########################################
# Ejercicio 3 : Generar un arreglo de dimension 20, llenarlo con valores al azar, mostrar por separado el contenido en sus posiciones pares y de las posiciones impares
#########################################
import random

def generar_arreglo_aleatorio():
    arreglo = [random.randint(1, 100) for _ in range(20)]
    return arreglo
def mostrar_posiciones_pares_impares(arreglo):
    print("Posiciones pares:")
    for i in range(0, len(arreglo), 2):
        print(f"Posicion {i}: {arreglo[i]}")
    
    print("\nPosiciones impares:")
    for i in range(1, len(arreglo), 2):
        print(f"Posicion {i}: {arreglo[i]}")

#########################################
# Ejercicio 4 : Generar un arreglo de dimension 20, llenarlo con valores al azar y decir cuantos valores pares contiene y cuantos impares
#########################################
def contar_pares_impares(arreglo):
    contador_pares = 0
    contador_impares = 0
    
    for numero in arreglo:
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
            
    print(f"Cantidad de valores pares: {contador_pares}")
    print(f"Cantidad de valores impares: {contador_impares}")

#########################################
# Ejercicio 5 : Llenar un arreglo de dimension 5 con numero impares y luego mostrarlo en modo invertido
#########################################
def llenar_arreglo_impares():
    arreglo = []
    for i in range(5):
        numero = int(input(f"Ingrese el numero impar {i + 1}: "))
        while numero % 2 == 0:  
            print("El numero ingresado no es impar. Intente nuevamente.")
            numero = int(input(f"Ingrese el numero impar {i + 1}: "))
        arreglo.append(numero)
    
    print("Arreglo en modo invertido:", arreglo[::-1])

#########################################
# Ejercicio 6 : Determinar el promedio de 10 notas ingresadas en un arreglo, indicando aprobado o desaprobado. Siendo el aprobado un promedio mayor al 60%
#########################################
def calcular_promedio_notas():
    notas = []
    for i in range(10):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")
    
    if promedio > 60:
        print("Aprobado")
    else:
        print("Desaprobado")

#########################################
# Ejercicio 7 : Dadas las siguientes notas almacenadas en un arrego, [33, 11, 20, 2, 15, 1, 12, 11, 8, 14, 10] Eliminar la nota mas baja sin usar la funcion min e imprimirla, luego calcular el promedio de notas
#########################################
def eliminar_nota_mas_baja(notas):
    nota_mas_baja = notas[0]
    for nota in notas:
        if nota < nota_mas_baja:
            nota_mas_baja = nota
            
    notas.remove(nota_mas_baja)
    print(f"Nota mas baja eliminada: {nota_mas_baja}")
    
    promedio = sum(notas) / len(notas)
    print(f"Promedio de notas: {promedio:.2f}")
notas = [33, 11, 20, 2, 15, 1, 12, 11, 8, 14, 10]
eliminar_nota_mas_baja(notas)

#########################################
# Ejercicio 8 : Ingresar 12 valores en un arreglo (matriz) de 4x3 y mostarlo en pantalla
#########################################
def ingresar_matriz():
    matriz = []
    for i in range(4):
        fila = []
        for j in range(3):
            valor = int(input(f"Ingrese el valor para la posicion ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    
    print("Matriz ingresada:")
    for fila in matriz:
        print(fila)
ingresar_matriz()

###########################################################################################################################

# Numpy arrays

# Sin utilizar ninguna funcion sofisticada de Numpy, usar bucles y el acceso individual a cada elemento a traves de su posicion dentro del array

#########################################
# Ejercicio 9 : Pedirle 6 numeros enteros al usuario y guardarlos en una lista. Crear un array de una dimension en base a dicha lista
#########################################
import numpy as np

def crear_array_desde_lista():
    numeros = []
    for i in range(6):
        numero = int(input(f"Ingrese el numero entero {i + 1}: "))
        numeros.append(numero)
    
    array = np.array(numeros)
    print("Array creado:", array)
crear_array_desde_lista()

#########################################
# Ejercicio 10 : Teniendo una lista con las alturas de los miembros de mi familia [181.5, 72, 34.7, 171.3, 160.1] crear un array a partir de ella y mostrar sus atributos, el tipo de datos, tanto del array como de sus elementos. Mostrar el total de familiares cargados en el array
#########################################
import numpy as np

def analizar_array_alturas():
    alturas = [181.5, 72, 34.7, 171.3, 160.1]
    array_alturas = np.array(alturas)
    
    print("Array de alturas:", array_alturas)
    print("Tipo de datos del array:", array_alturas.dtype)
    print("Tipo de datos de los elementos:", type(array_alturas[0]))
    print("Total de familiares cargados en el array:", len(array_alturas))
analizar_array_alturas()

#########################################
# Ejercicio 11 : Crear un array de 3 dimensiones, que tenga 3 matrices de 2 filas por 4 columnas, llenarlo de ceros
#########################################
import numpy as np

def crear_array_3d():
    array_3d = np.zeros((3, 2, 4))
    print("Array de 3 dimensiones lleno de ceros:")
    print(array_3d)
crear_array_3d()

#########################################
# Ejercicio 12 : Crear una matriz de 4,6 con valores al azar que pertencen al intervalo [0,1]
#########################################
import numpy as np

def crear_matriz_aleatoria():
    matriz_aleatoria = np.random.rand(4, 6)
    print("Matriz de 4x6 con valores al azar en el intervalo [0,1]:")
    print(matriz_aleatoria)
crear_matriz_aleatoria()

#########################################
# Ejercicio 13 : Crear un vector con un total de 25 elementos equidistantes en el intervalo [1, 6] Graficar
#########################################
import numpy as np
import matplotlib.pyplot as plt

def crear_vector_equidistante():
    vector = np.linspace(1, 6, 25)
    print("Vector con 25 elementos equidistantes en el intervalo [1, 6]:")
    print(vector)
    
    plt.plot(vector, np.zeros_like(vector), 'o')
    plt.title('Vector Equidistante')
    plt.xlabel('Valor')
    plt.yticks([])
    plt.grid()
    plt.show()
crear_vector_equidistante()

#########################################
# Ejercicio 14 : Crear un vector con numeros enteros al azar entre 0 y 5, luego reemplazar los 0 con el valor -1
#########################################
import numpy as np

def reemplazar_ceros_con_menos_uno():
    vector = np.random.randint(0, 6, size=10)
    print("Vector original:", vector)
    
    vector[vector == 0] = -1
    print("Vector despues de reemplazar 0 con -1:", vector)
reemplazar_ceros_con_menos_uno()

#########################################
# Ejercicio 15 : Crear una lista de 3 numeros al azar y un vector con 3 numeros enteros al azar, que sucede si suma la lista a si misma? lista + lista, y si se hace lo mismo con el vector?
#########################################
import numpy as np

def sumar_lista_y_vector():
    lista = [np.random.randint(0, 10) for _ in range(3)]
    vector = np.random.randint(0, 10, size=3)
    
    print("Lista original:", lista)
    print("Vector original:", vector)
    
    suma_lista = lista + lista
    suma_vector = vector + vector
    
    print("Suma de la lista consigo misma:", suma_lista)
    print("Suma del vector consigo mismo:", suma_vector)
sumar_lista_y_vector()

#Lo que sucede es que al sumar la lista consigo misma, se realiza una concatenacion de la lista, mientras que al sumar el vector consigo mismo, se realiza una suma elemento a elemento, lo que da como resultado un nuevo vector con el doble de cada elemento original

#########################################
# Ejercicio 16 : Crear una matriz de 3x3 con valores que van del 1 al 9
#########################################
import numpy as np

def crear_matriz_3x3():
    matriz = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    print("Matriz de 3x3 con valores del 1 al 9:")
    print(matriz)
crear_matriz_3x3()

#########################################
# Ejercicio 17 : Crear una matriz de 16 x 20 con numeros al azar, distinto al tipo de datos de float64
#########################################
import numpy as np

def crear_matriz_16x20():
    matriz = np.random.randint(0, 100, size=(16, 20), dtype=np.int32)
    print("Matriz de 16x20 con numeros al azar (tipo de datos int32):")
    print(matriz)
crear_matriz_16x20()

#########################################
# Ejercicio 18 : Crear un array de 5 filas y 6 columnas llenarlo con valores numericos enteros al azar entre 1 y 6, luego reemplazar los valores en la fila 5 por el valor 0
#########################################
import numpy as np

def reemplazar_fila_por_ceros():
    array = np.random.randint(1, 7, size=(5, 6))
    print("Array original:")
    print(array)
    
    array[4, :] = 0
    print("Array despues de reemplazar la fila 5 por ceros:")
    print(array)
reemplazar_fila_por_ceros()

#########################################
# Ejercicio 19 : Generar un array de 100 elementos organizados en 10 filas y 10 columnas,empezando en 0. Llenar su diagonal con el valor 1.5
#########################################
import numpy as np

def generar_array_diagonal():
    array = np.zeros((10, 10))
    np.fill_diagonal(array, 1.5)
    print("Array de 10x10 con diagonal llena de 1.5:")
    print(array)
generar_array_diagonal()

#########################################
# Ejercicio 20 : Crear una funcion que realice la suma de dos arrays de dimension 1 y devuelva el array resultante. Sin utilizar el operador de suma, si no creando un algoritmo que hiciese la sumar lugar a lugar
#########################################
import numpy as np

def sumar_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Los arrays deben tener la misma longitud")
    
    resultado = np.zeros(len(array1))
    for i in range(len(array1)):
        resultado[i] = array1[i] + array2[i]
    
    return resultado
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
resultado = sumar_arrays(array1, array2)
print("Resultado de la suma de los arrays:", resultado)

#########################################
# Ejercicio 21 : Crear una funcion que realice un producto entre dos arrays de dimension 1 y devuelva el vector resultante. Sin utilizar el operador *, creando un algoritmo que hiciese el producto lugar a lugar. 
#########################################
import numpy as np

def producto_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Los arrays deben tener la misma longitud")
    
    resultado = np.zeros(len(array1))
    for i in range(len(array1)):
        resultado[i] = array1[i] * array2[i]
    
    return resultado
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
resultado = producto_arrays(array1, array2)
print("Resultado del producto de los arrays:", resultado)

#########################################
# Ejercicio 22 : Al ejercicio anterior, agregarle una funcion que permita realizar la suma de elementos lugar a lugar, de dos arrays de dimension 2
#########################################
import numpy as np

def sumar_arrays_2d(array1, array2):
    if array1.shape != array2.shape:
        raise ValueError("Los arrays deben tener la misma forma")
    
    resultado = np.zeros(array1.shape)
    for i in range(array1.shape[0]):
        for j in range(array1.shape[1]):
            resultado[i, j] = array1[i, j] + array2[i, j]
    
    return resultado
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
resultado = sumar_arrays_2d(array1, array2)
print("Resultado de la suma de los arrays 2D:")
print(resultado)

#########################################
# Ejercicio 23 : Mostrar en pantalla una matriz de 6 x 6 con valores de 1 y 0, donde los valores de 1 se encuentren en la diagonal y los valores de 0 en el resto de la matriz
#########################################
import numpy as np

def mostrar_matriz_diagonal():
    matriz = np.zeros((6, 6), dtype=int)
    np.fill_diagonal(matriz, 1)
    print("Matriz de 6x6:")
    print(matriz)
mostrar_matriz_diagonal()

#########################################
# Ejercicio 24 : Mostrar en pantalla una matriz de 5x5 con valores de 1 y 0, donde la primer fila sea 1, despues 0 y asi sucesivamente
#########################################
import numpy as np

def mostrar_matriz_alternada():
    matriz = np.zeros((5, 5), dtype=int)
    for i in range(5):
        if i % 2 == 0:
            matriz[i, :] = 1
    print("Matriz de 5x5 con filas alternadas")
    print(matriz)
mostrar_matriz_alternada()

#########################################
# Ejercicio 25 : Mostrar en pantalla una matriz de 5x5 donde los valores 1 y 0 se vayan intercalando tanto en filas como en columnas, de tal forma que se forme un patron de tablero de ajedrez
#########################################
import numpy as np

def mostrar_matriz():
    matriz = np.zeros((5, 5), dtype=int)
    for i in range(5):
        for j in range(5):
            if (i + j) % 2 == 0:
                matriz[i, j] = 1
    print("Matriz de 5x5")
    print(matriz)
mostrar_matriz()

###########################################################################################################################

# Variado

#########################################
# Ejercicio 26 : Se desea graficar dos funciones para los mismos datos de x. Una es la funcion exponencial f(x) = 2^x y la otra funcion de logaritmo natural f(x) = ln(x), ambas deben ser graficadas en un intervalo positivo para los mismos valores de x que estaran en el rango [1.00,50.5] Los datos deberan ser almacenados en una matriz de 3 columnas, una columna para cada dato, por, al menos, 100 filas. Esta matriz (Numpy array) debera ser generado por usted.
#########################################
import numpy as np

def graficar_funciones():
    x = np.linspace(1.00, 50.5, 100)
    f_exponencial = 2 ** x
    f_logaritmo = np.log(x)
    
    matriz = np.column_stack((x, f_exponencial, f_logaritmo))
    
    print("Matriz con datos de x, f(x) exponencial y f(x) logaritmo:")
    print(matriz)
graficar_funciones()

###########################################################################################################################

# Preguntas de Revision

#########################################
# Ejercicio 27 : Existe relacion alguna entre la dimension de un array la cantidad de bucles necesarios para su manipulacion?
#########################################
# Si, a medida que aumenta la dimension de un array, se requieren mas bucles para manipularlo, especialmente si se desea acceder a elementos especificos o realizar operaciones complejas. Por ejemplo, un array de una dimension puede ser manipulado con un solo bucle, mientras que un array de dos dimensiones puede requerir dos bucles anidados para recorrer filas y columnas, y un array de tres dimensiones o mas puede requerir aun mas bucles anidados para recorrer todas las dimensiones. Existen tecnicas y funciones en bibliotecas como Numpy que permiten manipular arrays de alta dimension sin necesidad de usar multiples bucles explicitos lo que puede mejorar la eficiencia del codigo

#########################################
# Ejercicio 28 : Dada una matriz cuadrada, de dos dimensiones, si solo quiero modificar su diagonal. Necesito 2 bucles o 1 solo?
#########################################
# Solo se necesita un bucle para modificar la diagonal de una matriz cuadrada, ya que los elementos de la diagonal se encuentran en las posiciones donde el indice de fila es igual al indice de columna. Por ejemplo, para una matriz de tamaño n x n, se puede usar un solo bucle que recorra desde 0 hasta n-1 y modificar los elementos en las posiciones (i, i) para i en ese rango

#########################################
# Ejercicio 29 : Que suele ser primero, la fila o la columna, en la notacion de indices de un array de 2 dimensiones?
#########################################
# En la notacion de indices de un array de 2 dimensiones, la fila suele ser la primera, seguida por la columna. Es decir, el indice de fila se coloca antes del indice de columna