# Introduccion al bucle precondicional: while

#########################################
# Ejercicio 1 : Mostrar en pantalla los numeros del 1 al 50. Generar dos versiones, una con el bucle for, y otra con el bucle while. Que diferencias tienen?
#########################################
#Version con bucle for
for i in range (1, 51):
    print (i)

#Version con bucle while
i = 1
while i <= 50:
    print (i)
    i = i + 1

#########################################
# Ejercicio 2 : Mostrar en pantalla la siguiente sencuencia de valores, todos en una sola linea, separados por una coma. 10,20,30,40,50,60,70,80,90,100
#########################################
i = 10                 
while i <= 100:        
    if i == 100:       
        print(i)
    else:
        print(i, end=",")
    
    i = i + 10

#########################################
# Ejercicio 3 : Pedir 6 numeros al usuario. Almacenarlos en una lista
#########################################
numeros = []
i = 0 

while i < 6:
    n = int(input(f"Ingrese el número {i+1}: "))
    
    numeros.append(n)
    
    i = i + 1 
