#import sys
#sys.path.append(r"C:\FACULTAD\Ingenieria en Sistemas\Algoritmos y Estructuras de datos\fragmento_hobbit.txt\"

#########################################
# Ejercicio 1 : Mostrar el contenido del archivo fragmento_hobbit.txt y determinar cuantas lineas de texto hay mediante codigo y mostrar en pantalla
#########################################
def mostrar_contenido_archivo():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\fragmento_hobbit.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("Contenido del archivo:")
        for linea in lineas:
            print(linea.strip())
        print(f"\nCantidad de líneas: {len(lineas)}")

#########################################
# Ejercicio 2 : Crear un archivo de texto con el bloc de notas y crear un programa que muestre en pantalla el contenido linea por linea , mostrar el total de lineas. texto_prueba.txt
#########################################
def mostrar_contenido_archivo():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\texto_prueba.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("Contenido del archivo:")
        for linea in lineas:
            print(linea.strip())
        print(f"\nCantidad de líneas: {len(lineas)}")
if __name__ == "__main__":
    mostrar_contenido_archivo()

#########################################
# Ejercicio 3 : Crear un programa que genere un archivo de texto llamado numeros.txt con 10 numeros enteros guardados, uno por linea
#########################################
def archivo_numeros():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\numeros.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{i}\n")
    print("Archivo numeros.txt creado con exito.")
if __name__ == "__main__":
    archivo_numeros()

#########################################
# Ejercicio 4 : Crear un programa que le pida al usuario 5 colores y los guarde en un archivo de texto llamado colores.txt
#########################################
def guardar_colores():
    colores = []
    for i in range(5):
        color = input(f"Ingrese el color {i+1}: ")
        colores.append(color)
    
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\colores.txt", "w") as archivo:
        for color in colores:
            archivo.write(f"{color}\n")
    print("Archivo colores.txt creado con exito.")
if __name__ == "__main__":
    guardar_colores()

#########################################
# Ejercicio 5 : Crear un programa que dado un archivo de numeros con valores entre 1 y 10, determine cuantos numeros iguales a 5 hay en el archivo
#########################################
def contar_numero():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\numeros.txt", "r") as archivo:
        lineas = archivo.readlines()
        contador_cinco = sum(1 for linea in lineas if linea.strip() == "5")
    print(f"Cantidad de numeros iguales a 5: {contador_cinco}")
if __name__ == "__main__":
    contar_numero()

#########################################
# Ejercicio 6 : Crear un programa que lea un archivo de texto y determine el valor promedio y suma de todos ellos
#########################################
def calcular_promedio():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\listado.txt", "r") as archivo:
        lineas = archivo.readlines()
        total_calificaciones = 0
        contador_calificaciones = 0
        
        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                try:
                    calificacion = float(partes[1].strip())
                    total_calificaciones += calificacion
                    contador_calificaciones += 1
                except ValueError:
                    print(f"Calificacion no valida en la linea: {linea.strip()}")
        
        if contador_calificaciones > 0:
            promedio = total_calificaciones / contador_calificaciones
            print(f"Promedio de calificaciones: {promedio:.2f}")
            print(f"Suma de calificaciones: {total_calificaciones:.2f}")
        else:
            print("No se encontraron calificaciones validas.")
if __name__ == "__main__":
    calcular_promedio()

#########################################
# Ejercicio 7 : Crear un programa que permita elegir el color de una lista de 10 colores. Por defecto el programa la primera vez que se inicia empieza mostrando el color en pantalla azul, luego cada vez que se ejecuta mostrara en pantalla el color seleccionado por el usuario
#########################################
def elegir_color():
    colores = ["azul", "rojo", "verde", "amarillo", "naranja", "morado", "rosa", "negro", "blanco", "gris"]
    try:
        with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\color_seleccionado.txt", "r") as archivo:
            color_actual = archivo.read().strip()
    except FileNotFoundError:
        color_actual = "azul"
    print(f"Color actual: {color_actual}")
    print("Colores disponibles:")
    for i, color in enumerate(colores, start=1):
        print(f"{i}. {color}")
    seleccion = int(input("Seleccione un color por numero: "))
    if 1 <= seleccion <= len(colores):
        color_seleccionado = colores[seleccion - 1]
        with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\color_seleccionado.txt", "w") as archivo:
            archivo.write(color_seleccionado)
        print(f"Color seleccionado: {color_seleccionado}")
    else:
        print("Seleccion no valida.")
if __name__ == "__main__":
    elegir_color()
    
#########################################
# Ejercicio 8 : Generar dos archivos diferentes, uno llamado pesos.txt que contendra 50 valores para designar los pesos de 50 personas, otro llamado alturas.txt que contendra para dichas 50 personas las alturas en cm correspondientes. Generar un tercer archivo llamado bmi.txt que tendra calculados los BMI de cada persona. Permitir al usuario ingresar un numero n (del 1 al 50) para mostrale el bmi, traido desde el archivo de bmi.txt que ya genero el programa.
#########################################
def generar_archivos():
    import random
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\pesos.txt", "w") as archivo_pesos, open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\alturas.txt", "w") as archivo_alturas:
        for _ in range(50):
            peso = random.uniform(50, 100)
            altura = random.uniform(150, 200)
            archivo_pesos.write(f"{peso:.2f}\n")
            archivo_alturas.write(f"{altura:.2f}\n")
    print("Archivos pesos.txt y alturas.txt generados con exito.")
def calcular_bmi():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\pesos.txt", "r") as archivo_pesos, open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\alturas.txt", "r") as archivo_alturas, open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\bmi.txt", "w") as archivo_bmi:
        pesos = [float(linea.strip()) for linea in archivo_pesos.readlines()]
        alturas = [float(linea.strip()) for linea in archivo_alturas.readlines()]
        for peso, altura in zip(pesos, alturas):
            altura_m = altura / 100
            bmi = peso / (altura_m ** 2)
            archivo_bmi.write(f"{bmi:.2f}\n")
    print("Archivo bmi.txt generado con exito.")
def mostrar_bmi():
    n = int(input("Ingrese un numero del 1 al 50 para mostrar el BMI: "))
    if 1 <= n <= 50:
        with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\bmi.txt", "r") as archivo_bmi:
            lineas = archivo_bmi.readlines()
            bmi_seleccionado = lineas[n - 1].strip()
            print(f"BMI de la persona {n}: {bmi_seleccionado}")
    else:
        print("Numero no valido. Por favor ingrese un numero del 1 al 50.")
if __name__ == "__main__":
    generar_archivos()
    calcular_bmi()
    mostrar_bmi()

###########################################################################################################################

# Procedimientos

#########################################
# Ejercicio 9 : Crear un procedimiento que se encargue de imprimir un menu de opciones en pantalla. Puede elegir entre un menu de bebidas de un kiosco, menu de pizzas o un menu de operaciones aritmeticas a realizar entre dos numeros. El menu debe tener al menos unas 5 opciones, incluir una opcion de salir
#########################################
def mostrar_menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Menu de bebidas")
        print("2. Menu de pizzas")
        print("3. Operaciones aritmeticas")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print("\nMenu de bebidas:")
            print("- Coca Cola")
            print("- Pepsi")
            print("- Agua")
            print("- Jugo")
            print("- Cafe")
        elif opcion == "2":
            print("\nMenu de pizzas:")
            print("- Especial")
            print("- Jamon y Queso")
            print("- Vegetariana")
            print("- Cuatro quesos")
            print("- Fugazzeta")
        elif opcion == "3":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            print(f"Suma: {num1 + num2}")
            print(f"Resta: {num1 - num2}")
            print(f"Multiplicacion: {num1 * num2}")
            if num2 != 0:
                print(f"Division: {num1 / num2}")
            else:
                print("Division por cero no es posible.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor seleccione una opcion del menu.")
if __name__ == "__main__":
    mostrar_menu()

#########################################
# Ejercicio 10 : Realizar un programa que permita al usuario ingresar una longitud e imprima en pantalla un rectangulo de numerales en, sin relleno
#########################################
def imprimir_rectangulo():
    longitud = int(input("Ingrese la longitud del rectangulo: "))
    if longitud < 2:
        print("La longitud debe ser al menos 2 para formar un rectangulo.")
        return
    print("#" * longitud)
    for _ in range(longitud - 2):
        print("#" + " " * (longitud - 2) + "#")
    print("#" * longitud)
if __name__ == "__main__":
    imprimir_rectangulo()

#########################################
# Ejercicio 11 : Escribir un procedimiento que tome dos numeros, inicio y fin, e imprima en pantalla la secuencia de inicio hasta fin en la izquierda, y a su lado la sencuencia inversa fin hasta inicio
#########################################
def imprimir_secuencias():
    inicio = int(input("Ingrese el numero de inicio: "))
    fin = int(input("Ingrese el numero de fin: "))
    if inicio > fin:
        print("El numero de inicio debe ser menor o igual al numero de fin.")
        return
    for i in range(inicio, fin + 1):
        print(f"{i} {' ' * (fin - i)} {fin - (i - inicio)}")
if __name__ == "__main__":
    imprimir_secuencias()

###########################################################################################################################

# Alcance de Variables e Identificadores

#########################################
# Ejercicio 12 : Determine si este fragmento de codigo da error y en caso afirmativo, explicar por que
#########################################
def imprimir_nro():
    n = 1
    print("El primero numero es: ", n)

imprimir_nro()
print("El primer numero es: ", n)     # Esto dara un error porque la variable 'n' esta definida dentro de la funcion 'imprimir_nro' y no es accesible fuera de ella

#########################################
# Ejercicio 13 : Que imprimira en pantalla el siguiente codigo? Cual es el alcance de la variable frase? Es correcto el codigo?
#########################################
frase = "Hola" 

def proc():
    frase = "Es un lindo dia"
    print(frase)

    # La variable 'frase' dentro de la funcion 'proc' tiene un alcance local, por lo que al imprimir 'frase' dentro de la funcion se mostrara "Es un lindo dia". El codigo es correcto y no dara error

#########################################
# Ejercicio 14 : Determine cuales variables son locales y cuales son globales en el siguiente codigo
#########################################
saludo = "Hola"

def saludar_mundo():
    mundo = "Mundo !"
    print(saludo, mundo)

def saludar_nombre(nombre):
    print(saludo, nombre)

saludar_mundo()
saludar_nombre("Totoro")
# La variable 'saludo' es una variable global, ya que esta definida fuera de cualquier funcion y es accesible desde cualquier parte del codigo. Las variables 'mundo' y 'nombre' son variables locales, ya que estan definidas dentro de las funciones 'saludar_mundo' y 'saludar_nombre', y solo son accesibles dentro de esas funciones

#########################################
# Ejercicio 15 : De un pequeño codigo con una funcion o procedimiento inventado, que tenga variables loclaes y globales
#########################################
contador_global = 0

def incrementar_contador():
    global contador_global
    contador_global += 1
    print(f"Contador global incrementado: {contador_global}")
def mostrar_contador():
    print(f"Contador global actual: {contador_global}")
incrementar_contador()  # Incrementa el contador global a 1
mostrar_contador()     # Muestra el contador global actual (1)
incrementar_contador()  # Incrementa el contador global a 2
mostrar_contador()     # Muestra el contador global actual (2)

# En este codigo, 'contador_global' es una variable global que se puede modificar dentro de la funcion 'incrementar_contador' utilizando la palabra clave 'global'. La funcion 'mostrar_contador' accede a la variable global para mostrar su valor actual

#########################################
# Ejercicio 16 : Que imprimira en pantalla el siguiente codigo? Determine el alcance de cada variable
#########################################
x = 3

def p1():
    y = x + 1
    print(x)

    def p2():
        x = 1
        print(y)
        print(x)
    
    p2()
p1()

# El codigo imprimira: 3, 4, 1. La variable 'x' tiene un alcance global, ya que esta definida fuera de cualquier funcion. La variable 'y' tiene un alcance local dentro de la funcion 'p1', y la variable 'x' dentro de la funcion 'p2' tiene un alcance local a esa funcion, por lo que no afecta a la variable global 'x'

###########################################################################################################################

# Integrando conceptos 

#########################################
# Ejercicio 17 : Generar un archivo de texto, llamado datos.txt, que constara de las siguientes columnas, cada una separada por coma: x, y. Los valores de x iniciaran en 0.2 hasta llegar a 100.5 en incrementos de 0.3. Los valores de y seran generados por la funcion sigmoidea y = 1 / 1 + e ^(-x). Luego, generar un programa que lea el archivo de texto y muestre en pantalla el valor de x e y para cada linea del archivo
#########################################
import math
def generar_datos():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\datos.txt", "w") as archivo:
        x = 0.2
        while x <= 100.5:
            y = 1 / (1 + math.exp(-x))
            archivo.write(f"{x:.1f},{y:.6f}\n")
            x += 0.3
    print("Archivo datos.txt generado con exito.")
def mostrar_datos():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\datos.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("Contenido del archivo datos.txt:")
        for linea in lineas:
            x, y = linea.strip().split(",")
            print(f"{x}, {y}")
if __name__ == "__main__":
    generar_datos()
    mostrar_datos()
