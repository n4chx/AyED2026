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
    