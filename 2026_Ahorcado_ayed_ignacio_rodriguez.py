#Importamos la libreria random para elegir una palabra al azar de la lista
import random

#Definimos una lista de palabras posibles para el juego y una funcion al azar para elegir una de ellas
def elegir_palabra():
	palabras = [
		"python",
		"ahorcado",
		"computadora",
		"programacion",
		"algoritmo",
		"sistemas",
		"ingles",
		"algebra",
		"universidad",
		"programador",
	]
	return random.choice(palabras)

#Muestra el estado actual de la palabra y va agregando las letras adivinadas o el guin bajo si aun no se adivina
def mostrar_estado(palabra, letras_adivinadas):
	resultado = ""
	for letra in palabra:
		if letra in letras_adivinadas:
			resultado += letra + " "
		else:
			resultado += "_ "
	return resultado.strip()

#Pedimos al jugador que ingrese el numero de intentos que quiera tener para adivinar la palabara
def pedir_intentos():
	while True:
		entrada = input("Cuantos intentos quieres tener? (1-30): ").strip()
		if entrada.isdigit():
			numero = int(entrada)
			if 1 <= numero <= 30:
				return numero
		print("Ingresa un numero entre 1 y 30.")

#Pedimos al jugador que ingrese una letra alfabetica y verificamos las condiciones
def pedir_letra(letras_adivinadas):
	while True:
		letra = input("Adivina una letra: ").strip().lower()
		if len(letra) != 1:
			print("Debes ingresar solo una letra.")
		elif not letra.isalpha():
			print("Ingresa una letra del abecedario.")
		elif letra in letras_adivinadas:
			print("Ya probaste esa letra. Intenta otra.")
		else:
			return letra

#Seteamos las variables a usar
def juego_ahorcado():
	print("=== Juego del Ahorcado ===")
	intentos = pedir_intentos()
	palabra = elegir_palabra()
	letras_adivinadas = set()
	intentos_restantes = intentos

	while intentos_restantes > 0: #Mientras el jugador tenga intentos restantes se muestra el estado de la palabra y se le pide que adivine una letra
		estado = mostrar_estado(palabra, letras_adivinadas)
		print("\nPalabra:", estado)
		print("Intentos restantes:", intentos_restantes)

		if all(letra in letras_adivinadas for letra in palabra): #Si el jugador adivina todas las letras de la palabra se termina el juego y se muestra un mensaje de felicitaciones
			print("\n¡Felicidades! Adivinaste la palabra:", palabra)
			break

		#Si se ha adivinado al menos el 70% de la palabra se puede arriesgar para adivinar la palabra completa
		letras_reveladas = sum(1 for c in palabra if c in letras_adivinadas)
		if len(palabra) > 0 and (letras_reveladas / len(palabra)) >= 0.7:
			porcentaje = int((letras_reveladas / len(palabra)) * 100)
			respuesta = input(f"Has descubierto {letras_reveladas} de {len(palabra)} letras ({porcentaje}%). Quieres arriesgar y adivinar la palabra completa? (s/n): ").strip().lower()
			if respuesta == 's':
				intento_palabra = input("Ingresa la palabra que crees que es: ").strip().lower()
				if intento_palabra == palabra:
					print("\nFelicidades! Adivinaste la palabra completa:", palabra) #Si el jugador adivina la palabra completa se termina el juego y se muestra un mensaje de felicitaciones
					return
				else:
					print("\nRespuesta incorrecta. Game over.") #Si el jugador se arriesga a adivinar la palabra completa y falla se termina el juego
					intentos_restantes = 0
					break

		letra = pedir_letra(letras_adivinadas) #Pedimos una letra al jugador y verificamos si esta en la palabra o no

		if letra in palabra:
			letras_adivinadas.add(letra)
			print("¡Bien! La letra", letra, "esta en la palabra.") #Si la letra esta en la palabra se agrega a la lista de letras adivinadas
		else:
			letras_adivinadas.add(letra)
			intentos_restantes -= 1
			print("La letra", letra, "no esta en la palabra.") #Si no, se resta un intento y se agrega a la lista para que no vuevla a probar la misma
	else:
		print("\nGame Over. La palabra secreta era:", palabra) #Si se quedan sin intentos se muestra la palabra secreta

	print("Gracias por jugar.")


if __name__ == "__main__":
	juego_ahorcado()