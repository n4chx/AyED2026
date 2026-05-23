#import sys
#sys.path.append(r"C:\FACULTAD\Ingenieria en Sistemas\Algoritmos y Estructuras de datos\fragmento_hobbit.txt\"


# Ejercicio 1 : Mostrar el contenido del archivo fragmento_hobbit.txt y determinar cuantas lineas de texto hay mediante codigo y mostrar en pantalla

def mostrar_contenido_archivo():
    with open(r"C:\FACULTAD\Ingenieria en Sistemas\Algoritmos y Estructuras de datos\fragmento_hobbit.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("Contenido del archivo:")
        for linea in lineas:
            print(linea.strip())
        print(f"\nCantidad de líneas: {len(lineas)}")
