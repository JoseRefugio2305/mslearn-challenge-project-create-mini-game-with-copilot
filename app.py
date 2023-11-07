#Crea una funcion que reciba una palabra y verifique si la palabra en minusculas se encuentra dentro de una lista de palabras que sea igual a ["piedra", "papel", "tijeras"]
def comprobar_palabra(palabra):
    #Crea una lista con las palabras que se pueden introducir
    palabras = ["piedra", "papel", "tijeras"]
    #Crea un bucle que se ejecute mientras la palabra introducida no este en la lista
    while palabra.lower() not in palabras:
        #Pregunta al usuario por una palabra
        palabra = input("Introduce una palabra válida: ")
    #Devuelve la palabra
    return palabra


#Crea una funcion llamada definir_ganador que reciba una palabra y que de forma aleatoria tome una palabra de una lista que sea igual a ["piedra", "papel","tijeras"] y que determine si el usuario gano, perdio o empato
def definir_ganador(palabra):
    #Importa la libreria random
    import random
    #Crea una lista con las palabras que se pueden introducir
    palabras = ["piedra", "papel", "tijeras"]
    #Crea una variable que almacena una palabra aleatoria de la lista
    palabra_aleatoria = random.choice(palabras)
    #Imprime la palabra aleatoria
    print("El ordenador ha elegido: " + palabra_aleatoria)
    #Si la palabra aleatoria es igual a la palabra introducida por el usuario, imprime que ha empatado ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    if palabra_aleatoria == palabra:
        print("Has empatado")
        return 0
    #Si la palabra aleatoria es igual a piedra y la palabra introducida por el usuario es igual a papel, imprime que ha ganado ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    elif palabra_aleatoria == "piedra" and palabra == "papel":
        print("Has ganado")
        return 1
    #Si la palabra aleatoria es igual a piedra y la palabra introducida por el usuario es igual a tijeras, imprime que ha perdido ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    elif palabra_aleatoria == "piedra" and palabra == "tijeras":
        print("Has perdido")
        return -1
    #Si la palabra aleatoria es igual a papel y la palabra introducida por el usuario es igual a tijeras, imprime que ha ganado ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    elif palabra_aleatoria == "papel" and palabra == "tijeras":
        print("Has ganado")
        return 1
    #Si la palabra aleatoria es igual a papel y la palabra introducida por el usuario es igual a piedra, imprime que ha perdido ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    elif palabra_aleatoria == "papel" and palabra == "piedra":
        print("Has perdido")
        return -1
    #Si la palabra aleatoria es igual a tijeras y la palabra introducida por el usuario es igual a piedra, imprime que ha ganado ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    elif palabra_aleatoria == "tijeras" and palabra == "piedra":
        print("Has ganado")
        return 1
    #Si la palabra aleatoria es igual a tijeras y la palabra introducida por el usuario es igual a papel, imprime que ha perdido ademas de retornar 0 si empata, 1 si gana y -1 si pierde
    elif palabra_aleatoria == "tijeras" and palabra == "papel":
        print("Has perdido")
        return -1


#Crea una funcion que le pida al usuario introducir una opcion para el juego de piedra papel o tijeras y que envie lo que el usuario introdujo a la funcion comprobar_palabra
def jugar():
    #Pregunta al usuario por una palabra
    palabra = input("Introduce una opcion (piedra, papel o tijeras): ")
    #Llama a la funcion comprobar_palabra y le envia la palabra introducida por el usuario
    palabra = comprobar_palabra(palabra)
    
    #llama a la funcion definir_ganador y le envia la palabra introducida por el usuario
    return definir_ganador(palabra)


#crea una variable que almacena el puntaje inicializada en 0
puntaje = 0

#Crea un bucle que se ejecute siempre y cuando el usuario introduzca que quiere seguir jugando
while True:
    #Llama a la funcion jugar y lo que retorne sumalo a puntaje
    puntaje += jugar()
    #Pregunta al usuario si quiere seguir jugando, si no quiere, rompe el bucle, si quiere, continua
    if input("¿Quieres seguir jugando? (s/n): ") == "n":
        break
#Imprime el valor de puntaje
print("Tu puntaje es: " + str(puntaje))
