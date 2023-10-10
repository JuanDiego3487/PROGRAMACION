#funcion para importar numeros
import random

#Funcion para el rango entre 1 a 1000 de intentos
def leerIntentos(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1 or n > 10 or n == "":
                print("Intentos alcanzados")
                continue
            return n
        except ValueError:
            print("Error, Total de intentos alcanzados")

#Funcion para leer la identificacion por el medio del nombre del usuario
def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def menu():
    while True:
        try:
            print("\n" )
            print("\nMENU" )
            print("1. Nombre del usuario: ")
            print("2. Lista de jugadores: ")
            print("3. Salir ")
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")