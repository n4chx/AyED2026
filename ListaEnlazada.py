# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:13:24 2023

@author: Carina Povarchik
"""
        
        
class ListaEnlazada:

    def __init__(self):
        self.cabeza = Nodo(None)

    def agregar(self, dato):
        nodo = Nodo(dato)
        
        nodo_aux = self.cabeza
        while nodo_aux.siguiente != None:
            nodo_aux = nodo_aux.siguiente

            # asignar el nuevo nodo al puntero del último
        nodo_aux.siguiente = nodo
        
    def display(self):
        # variable para la iteración
        nodo_aux = self.cabeza

        # iterar hasta alcanzar el final de la lista
        while nodo_aux != None:
            # imprimir la data del nodo
            print(nodo_aux.dato, end=' -> ')

            # mover la variable temporal al próximo nodo
            nodo_aux = nodo_aux.siguiente

        print('Null')

    def at(self, pos):  #obtener el elemento en la posición pos
        # variable para la iteración
        nodo_aux = self.cabeza

        contador = 0
        while nodo_aux != None:
            if contador == pos + 1:  # sumo uno, para no contar el nodo cabeza.
                return nodo_aux

            contador += 1

            nodo_aux = nodo_aux.siguiente

        raise Exception("Lista vacia o fuera de rango")   
        
    def __len__(self):
       nodo_aux = self.cabeza

       contador = 0
       while nodo_aux != None:
           nodo_aux = nodo_aux.siguiente
           contador += 1  
       
       # descontamos el nodo cabeza, que no lo estamos usando para guardar datos,
       # solo de inicio de la estructura
       return (contador - 1)  
           
        
class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

    def __str__(self)  :
        return str(self.dato)



# Ejemplo de uso
# milista = ListaEnlazada()

# milista.agregar(3)
# milista.agregar(7)
# milista.agregar(2)
# milista.display()
# print(milista.at(2))               
# print(len(milista))

