#import sys
#sys.path.append(r"C:\FACULTAD\Ingenieria en Sistemas\Algoritmos y Estructuras de datos\fragmento_hobbit.txt\"

#########################################
# Ejercicio 1 : Mostrar el contenido del archivo fragmento_hobbit.txt y determinar cuantas lineas de texto hay mediante codigo y mostrar en pantalla
#########################################
def mostrar_contenido_archivo():
    with open(r"C:\FACULTAD\Ingenieria en Sistemas\Algoritmos y Estructuras de datos\fragmento_hobbit.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("Contenido del archivo:")
        for linea in lineas:
            print(linea.strip())
        print(f"\nCantidad de líneas: {len(lineas)}")

#########################################
# Ejercicio 2 : Crear un archivo de texto con el bloc de notas y crear un programa que muestre en pantalla el contenido linea por linea , mostrar el total de lineas. texto_prueba.txt
#########################################
def mostrar_contenido_archivo_prueba():
    with open(r"D:\0Ingeniería en Sistemas\1ero\Algoritmos y Estructuras de datos\Algoritmos y Estructuras de datos\texto_prueba.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("Contenido del archivo:")
        for linea in lineas:
            print(linea.strip())
        print(f"\nCantidad de líneas: {len(lineas)}")

if __name__ == "__main__":
    mostrar_contenido_archivo()
    print("\n" + "="*50 + "\n")
    mostrar_contenido_archivo_prueba()
    
    