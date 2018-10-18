# Autor: Roberto Emmanuel González Muñoz
# Solución de problemas con ciclos while

import random
from random import randint


def dividir(dividendo, divisor):
    contador = 0
    dividendoOriginal = dividendo
    termina = False
    while not termina:
        contador += 1
        dividendo = dividendo - divisor
        if dividendo < divisor:
            print("%d / %d = %d , sobra %d" % (dividendoOriginal, divisor, contador, dividendo))
            termina = True
            return print("El resultado es: ", contador)


def encontrarMayor():
    datos = []
    numero = int(input("Valor [-1 termina]: "))
    while numero != -1:
        datos.append(numero)
        numero = int(input("Valor [-1 termina]: "))

    if len(datos) > 0:
        print("El mayor es: ", max(datos))

    elif numero == -1:
        print("No hay valor mayor")


def leerOpcionMenu():
    print("__________________________________________")
    print("Misión 07. Ciclos While")
    print("Autor: Roberto Emmanuel González Muñoz")
    print("Matrícula: A01376803")
    print("1. Calcular divisiones.")
    print("2. Encontrar el mayor.")
    print("0. Salir.")
    opcion = int(input("Teclea tu opción: "))
    print("__________________________________________")
    return opcion


def main():
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            print("Calculando Divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)

        elif opcion == 2:
            encontrarMayor()
        else:
            print("ERROR, Teclea 1, 2 o 3")
        opcion = leerOpcionMenu()
    print("Gracias por usar este programa, regresa pronto.")


main()