# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:22:56 2022

@author: Carina Povarchik

AyED PILA

Una Pila o stack es una estructura de datos lineal que sigue el orden LIFO
(Último en entrar, primero en salir), es decir, los elementos se pueden
insertar o quitar solo en un extremo de la misma.

La stack admite las siguientes operaciones estándar:

    push(e): Agrega un elemento e en el tope de mi lista
    pop(): Remueve el elemento del tope de mi lista y me lo devuelve.
    Tira error si la pila está vacía
    
    top(): Me trae el tope de la lista, sin quitarlo de la pila. Tira error si pila vacia
    (top o peek)
    
    is_empty(): Devuelve True si la pila está vacia.
    len(): Me devuelve el total de elementos en la pila. (len o size)


Implementada con listas, quedaría algo del estilo

Método de la Pila   =>    Implementación con Lista de Python
pila.push(e)                L.append(e)
pila.pop()                  L.pop( )
pila.top()                  L[−1]
pila.is_empty()             len(L) == 0
pila.len()                  len(L)

"""


class EmptyError(Exception):
    """ Error al intentar obtener un elemento, la Pila está vacía."""
    pass


# Implementación de stack personalizada en Python, con listas
class Pila:
 
    # Inicializador de mi pila
    def __init__(self):
        self.datos = []

    def push(self, elemento):
        #print(f'Insertando {elemento} en la pila…')
        self.datos.append(elemento)
 
    def pop(self):
        if self.is_empty():
            #o hago un raise Empty('Pila vacia!')
            print('Pila vacía! No es posible quitar nada de ella…')
            exit(-1)

        #print(f'Quitando {self.top()} de la pila.')
        return self.datos.pop()
 
    # Función para devolver el elemento superior de la stack, SIN quitarlo
    def top(self):
        if self.is_empty():
            # raise EmptyError('Pila vacia!')
            raise Exception()
            
        return self.datos[-1]
 
    def is_empty(self):
        return len(self.datos) == 0
 
    # Lo puedo usar como el len de siempre? len(pila) ??? en vez de pila.len()???
    def __len__(self):
        return len(self.datos)



# EJEMPLO DE USO
# pila1 = Pila()

# pila1.push(2)
# pila1.push(4)
# print(pila1.top())

# pila1.pop()
# pila1.pop()

# pila1.pop() #para ver cómo queda el raise EmptyError

