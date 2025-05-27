#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:48:07 2023

@author: laptop
"""

# 1. Contador de números pares e impares:
"""
Escribe un programa que utilice un bucle for o while para contar y mostrar 
la cantidad de números pares e impares en un rango específico, 
por ejemplo, del 1 al 100.
"""
contador = 1
contador_pares = 0
contador_impares = 0
lista_pares = []
lista_impares = []
while contador <= 100:
    if contador % 2 == 0:
        print(f"{contador} es par")
        contador_pares += 1
        lista_pares.append(contador)
    else:
        print(f"{contador} es impar")
        contador_impares += 1
        lista_impares.append(contador)
    contador += 1


contador_pares = 0
contador_impares = 0
lista_pares = []
lista_impares = []
for contador in range(1, 101):
    if contador % 2 == 0:
        print(f"{contador} es par")
        contador_pares += 1
        lista_pares.append(contador)
    else:
        print(f"{contador} es impar")
        contador_impares += 1
        lista_impares.append(contador)


# 2. Suma de números primos:
"""
Crea un programa que solicite al usuario un número y utilice un bucle 
while para sumar todos los números primos menores o iguales al número 
ingresado.
"""

numero = int(input("Ingrese un número: "))

factor = 2
es_primo=True
while factor < numero:
    if numero % factor == 0:
        print(f"{numero} no es primo", factor)
        es_primo=False
        break
    factor += 1

lista_primos = []
candidato_a_primo = 2
while candidato_a_primo < numero:
    factor = 2
    es_primo=True
    while factor < candidato_a_primo:
        if candidato_a_primo % factor == 0:
            print(f"{candidato_a_primo} no es primo", factor)
            es_primo=False
            break
        factor += 1
    if es_primo:
        lista_primos.append(candidato_a_primo)
    candidato_a_primo += 1


# 3. Tabla de multiplicar:
"""
Pide al usuario que ingrese un número y luego muestra la tabla de 
multiplicar de ese número del 1 al 10 utilizando un bucle for.
"""
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    print(str(numero) + " x " + str(i) + " = " + str(numero * i))
    print("{} x {} = {}".format(numero, i, numero * i))
    print("{numero} x {i} = {resultado}".format(numero=numero, i=i, resultado=numero * i))




# 4. Generador de patrones:
"""
Escribe un programa que solicite al usuario un número y utilice 
un bucle for o while para generar patrones como el siguiente, donde 
el número ingresado determine la cantidad de filas:
"""
1
22
333
4444
55555

numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    for j in range(i):
        print(i, end="")
    print()

for i in range(1, numero + 1):
    print(str(i) * i)

# 5. Adivina el número:
"""
Crea un juego en el que el programa genera un número aleatorio y el 
usuario tiene que adivinarlo. Utiliza un bucle while para que el usuario 
pueda seguir intentando hasta que adivine el número. Proporciona pistas 
para indicar si el número a adivinar es mayor o menor que el intento del 
usuario.
"""
from random import randint

numero_aleatorio = randint(0, 100)

# Pedir al usuario que adivine el número
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento == numero_aleatorio:
        print("¡Correcto! Adivinaste el número.")
        break
    elif intento < numero_aleatorio:
        print("El número a adivinar es mayor que", intento)
    else:
        print("El número a adivinar es menor que", intento)