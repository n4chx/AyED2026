# Pilas y Colas

# Pilas - LIFO (Last In First Out)
#########################################
# Ejercicio 1 : El usuario ingresa una palabra, almacenar dicha palabra, de a un caracter en una pila. Invertir la palabra y mostrarla en pantalla.
#########################################
palabra = input("Ingrese una palabra: ")
pila = []

for caracter in palabra:
    pila.append(caracter)

inversa = []
while pila:
    inversa.append(pila.pop())

print("Palabra invertida:", "".join(inversa))

#########################################
# Ejercicio 2 : Crear una funcion que determine si una palabra es palindromo o no. 
#########################################
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    pila = []
    
    for caracter in palabra:
        pila.append(caracter)
    
    inversa = []
    while pila:
        inversa.append(pila.pop())
    
    return "".join(inversa) == palabra

# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("La palabra es un palindromo.")
else:
    print("La palabra no es un palindromo.")

#########################################
# Ejercicio 3 : Un conductor maneja de un pueblo origen a un pueblo destino, pasando por varios pueblos. Una vez en el pueblo destino, el conductor debe regresar a casa por el mismo camino. Muestre el camino recorrido tanto de ida como de vuelta.
#########################################
pueblo_origen = input("Ingrese el nombre del pueblo de origen: ")
pueblo_destino = input("Ingrese el nombre del pueblo de destino: ")
pueblos_intermedios = []

while True:
    pueblo = input("Ingrese el nombre de un pueblo intermedio (o 'fin' para terminar): ")
    if pueblo == "fin":
        break
    pueblos_intermedios.append(pueblo)


print("Camino de ida:")
print(pueblo_origen, end=" -> ")
for pueblo in pueblos_intermedios:
    print(pueblo, end=" -> ")
print(pueblo_destino)

print("Camino de vuelta:")
print(pueblo_destino, end=" -> ")
for pueblo in reversed(pueblos_intermedios):
    print(pueblo, end=" -> ")
print(pueblo_origen)

#########################################
# Ejercicio 4 : Permite ingresar una cadena de caracteres y determine si los simbolos () y [] estan balanceados. Si no lo estan muestre el error indicando el simbolo faltante.
#########################################
def esta_balanceada(cadena):
    pila = []
    simbolos = {')': '(', ']': '['}
    
    for caracter in cadena:
        if caracter in "([":  
            pila.append(caracter)
        elif caracter in ")]":  
            if not pila or pila[-1] != simbolos[caracter]:
                return False, f"Error: simbolo faltante para '{caracter}'"
            pila.pop()
    
    if pila:
        return False, f"Error: simbolo faltante para '{pila[-1]}'"
    
    return True, "Los simbolos estan balanceados."

cadena = input("Ingrese una cadena de caracteres: ")
balanceada, mensaje = esta_balanceada(cadena)
if balanceada:
    print(mensaje)
else:
    print(mensaje)

#########################################
# Ejercicio 5 : Un almacen de amazon tiene capacidad para apilar n contenedores. Cada contenedor tiene un numero de identificacion. Cuando se desea retirar un contenedor especifico, deben retirarse primero los contenedores que estan encima de el y colocarlos en otra pila, efectuar el retiro y regresarlos. Codifique los metodos push() y pop() para gestionar los contenedores
#########################################
class Pila:
    def __init__(self):
        self.contenedores = []

    def push(self, contenedor):
        self.contenedores.append(contenedor)

    def pop(self):
        if not self.esta_vacia():
            return self.contenedores.pop()
        else:
            raise IndexError("La pila esta vacia.")

    def esta_vacia(self):
        return len(self.contenedores) == 0

    def retirar_contenedor(self, id_contenedor):
        pila_auxiliar = Pila()
        
        # Retirar contenedores hasta encontrar el deseado
        while not self.esta_vacia():
            contenedor_actual = self.pop()
            if contenedor_actual == id_contenedor:
                print(f"Contenedor {id_contenedor} retirado.")
                break
            else:
                pila_auxiliar.push(contenedor_actual)
        
        # Regresar los contenedores a la pila original
        while not pila_auxiliar.esta_vacia():
            self.push(pila_auxiliar.pop())

#########################################
# Ejercicio 6 : Dado un archivo de texto con algunas lineas de texto dentro, cualesquiera, realizar un programa que genere un archivo de texto llamado invertido.txt que contenga las lineas en orden inverso al archivo original
#########################################
def invertir_lineas_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    lineas_invertidas = lineas[::-1]
    
    with open('invertido.txt', 'w') as archivo_invertido:
        archivo_invertido.writelines(lineas_invertidas)

#########################################
# Ejercicio 7 : Implementar un verificador de codigo HTML para chequear que un archivo HTML sea valido. Luego el verificador debera pedir un archivo de texto con extension correspondiente .html y verificar su codigo html este correcto. 
#########################################
def verificar_codigo_html():
    nombre_archivo = input("Ingrese el nombre del archivo (con extension .html o .htm): ")
    
    if not (nombre_archivo.endswith('.html') or nombre_archivo.endswith('.htm')):
        print("Error: El archivo debe tener extension .htm o .html")
        return False
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("Error: No se encontro el archivo especificado.")
        return False
    pila = []
    i = 0
    while i < len(contenido):
        if contenido[i] == '<':
            fin_etiqueta = contenido.find('>', i)
            if fin_etiqueta != -1:
                etiqueta = contenido[i+1 : fin_etiqueta].strip()

                if etiqueta.startswith('/'):
                    nombre_etiqueta = etiqueta[1:].strip()
                    if len(pila) == 0:
                        print(f"Codigo Invalido: Se encontro </{nombre_etiqueta}> pero no hay etiquetas abiertas.")
                        return False
                    tope = pila.pop()
                    if tope != nombre_etiqueta:
                        print(f"Codigo Invalido: Se esperaba cerrar <{tope}> pero se cerro </{nombre_etiqueta}>.")
                        return False
                else:
                    pila.append(etiqueta)
                i = fin_etiqueta
        i += 1

    if len(pila) == 0:
        print("¡El codigo HTML es VaLIDO! Todas las etiquetas estan correctamente cerradas.")
        return True
    else:
        print(f"Codigo Invalido: Falto cerrar las siguientes etiquetas: {pila}")
        return False

verificar_codigo_html()

#########################################
# Ejercicio 8 : Implementar una calculadora de Notacion Polaca Inversa, usando la notacion de infijo
#########################################
def calcular_notacion_polaca_inversa(expresion):
    pila = []
    operadores = set(['+', '-', '*', '/'])

    for token in expresion.split():
        if token not in operadores:
            pila.append(float(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)

    return pila[0]

expresion = input("Ingrese una expresion en Notacion Polaca Inversa (RPN): ")
resultado = calcular_notacion_polaca_inversa(expresion)
print("Resultado:", resultado)

#########################################
# Ejercicio 9 : Implementar una funcion que invierta el orden de las palabras de una frase. Ejemplo: Si se recibe la frase "Buen dia!" retornar "dia! Buen"
#########################################
def invertir_palabras(frase):
    palabras = frase.split()
    palabras_invertidas = palabras[::-1]
    return " ".join(palabras_invertidas)

frase = input("Ingrese una frase: ")
frase_invertida = invertir_palabras(frase)
print("Frase invertida:", frase_invertida)

###########################################################################################################################
# Colas
# FIFO (First In First Out)
###########################################################################################################################

#########################################
# Ejercicio 10 : En una sala de espera de un consultorio se encuentran los pacientes que van a visitar a un medico. Simular la atencion de los mismos respetando el orde de llegada y determinar cuantos de ellos tienen obra social
#########################################
class Cola:
    def __init__(self):
        self.pacientes = []

    def encolar(self, paciente):
        self.pacientes.append(paciente)

    def desencolar(self):
        if not self.esta_vacia():
            return self.pacientes.pop(0)
        else:
            raise IndexError("La cola esta vacia.")

    def esta_vacia(self):
        return len(self.pacientes) == 0

    def contar_obra_social(self):
        return sum(1 for paciente in self.pacientes if paciente['obra_social'])
        
#########################################
# Ejercicio 11 : Se tiene una cola donde los hombres son muy traviesos, es por esto que se ordena dividir la cola en una de hombres y una de mujeras
#########################################
class ColaHombres(Cola):
    def encolar(self, paciente):
        if paciente['genero'] == 'hombre':
            super().encolar(paciente)
        else:
            raise ValueError("Solo se pueden encolar hombres en esta cola.")
            
class ColaMujeres(Cola):
    def encolar(self, paciente):
        if paciente['genero'] == 'mujer':
            super().encolar(paciente)
        else:
            raise ValueError("Solo se pueden encolar mujeres en esta cola.")

#########################################
# Ejercicio 12 : Modelar una cola generalizada. la cantidad de cartas que se reciben por persona, modificarla a otro valor distinto de 5
#########################################
class ColaGeneralizada:
    def __init__(self, max_cartas_por_persona=5):
        self.cola = []
        self.max_cartas_por_persona = max_cartas_por_persona

    def encolar(self, persona):
        if persona['cantidad_cartas'] > self.max_cartas_por_persona:
            raise ValueError(f"No se pueden recibir mas de {self.max_cartas_por_persona} cartas por persona.")
        self.cola.append(persona)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            raise IndexError("La cola esta vacia.")

    def esta_vacia(self):
        return len(self.cola) == 0

###########################################################################################################################
# Listas Enlazadas
###########################################################################################################################

#########################################
# Ejercicio 13 : Generar una lista enlazada con 8 numeros al azar enteros. Preguntarle al usuario cual numero desea obtener: el primero? el segundo? mostrarle el valor almacenado en la lista enlazada que pidio
#########################################
import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener(self, posicion):
        actual = self.cabeza
        for _ in range(posicion):
            if not actual:
                raise IndexError("Posicion fuera de rango.")
            actual = actual.siguiente
        if not actual:
            raise IndexError("Posicion fuera de rango.")
        return actual.valor

lista = ListaEnlazada()
for _ in range(8):
    lista.agregar(random.randint(1, 100))

try:
    posicion = int(input("Ingrese la posicion del numero que desea obtener (0-7): "))
    numero = lista.obtener(posicion)
    print(f"El numero en la posicion {posicion} es: {numero}")
except ValueError:
    print("Por favor, ingrese un numero valido.")
except IndexError as e:
    print(f"Error: {e}")

#########################################
# Ejercicio 14 : Pedir al usuario 6 numeros que representen la edad de 6 amigos. Guardarlos en una lista enlazada. Mostrar la edad del tercer amigo. Calcular la edad promedio del grupo de amigos
#########################################
lista_edades = ListaEnlazada()
for i in range(6):
    while True:
        try:
            edad = int(input(f"Ingrese la edad del amigo {i + 1}: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente nuevamente.")
                continue
            lista_edades.agregar(edad)
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

try:
    edad_tercer_amigo = lista_edades.obtener(2)
    print(f"La edad del tercer amigo es: {edad_tercer_amigo}")
    suma_edades = 0
    actual = lista_edades.cabeza
    while actual:
        suma_edades += actual.valor
        actual = actual.siguiente
    promedio = suma_edades / 6
    print(f"El promedio de las edades es: {promedio}")
except IndexError as e:
    print(f"Error: {e}")

