# Introduccion al bucle precondicional: while

#########################################
# Ejercicio 1 : Mostrar en pantalla los numeros del 1 al 50. Generar dos versiones, una con el bucle for y otra con el bucle while. Que diferencias tienen?
#########################################

# Version con el bucle for
for i in range(1, 51):
    print(i)

# Version con el bucle while
i = 1
while i <= 50:
    print(i)
    i += 1

# Diferencias: La version con el bucle for es mas compacta y facil de leer, ya que el bucle for esta diseñado para iterar sobre un rango de numeros

#########################################
# Ejercicio 2 : Mostrar en pantalla la siguiente secuencia de valores, todos en una sola linea, separados por una coma. 10,20,30,40,50,60,70,80,90,100
#########################################

