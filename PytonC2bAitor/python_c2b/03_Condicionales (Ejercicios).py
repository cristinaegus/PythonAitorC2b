
# 1. Crear una lista con 10 elementos numéricos.
# Lista de números aleatorios
import random
numeros = [random.randint(1, 30) for _ in range(10)]

# o crearlos "a mano"
numeros = [4, 29, 11, 21, 19, 28, 23, 15, 27, 27]
print(numeros)


# 2. Comprobar si el tercer elemento es mayor que el séptimo y crear una frase que
# muestre por escrito si el número es mayor o menor y el valor que toma el tercer elemento.
if numeros[2] > numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es mayor que el séptimo ({numeros[6]})")
else:
    print(f"El tercer elemento ({numeros[2]}) es menor que el séptimo ({numeros[6]})")

# 3. Invertir el orden de la lista y realizar la misma comprobación.
numeros.reverse()
print(numeros)
if numeros[2] > numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es mayor que el séptimo ({numeros[6]})")
else:
    print(f"El tercer elemento ({numeros[2]}) es menor que el séptimo ({numeros[6]})")

# 4. Añadir la posibilidad de que sea igual.
if numeros[2] > numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es mayor que el séptimo ({numeros[6]})")
elif numeros[2] == numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es igual que el séptimo ({numeros[6]})")
else:
    print(f"El tercer elemento ({numeros[2]}) es menor que el séptimo ({numeros[6]})")  



# 5. Transformar el séptimo número para que se satisfaga la igualdad.
numeros[6] = numeros[2]
print(numeros)

# 6. Realizar la comprobación.

