# Ejercicio 1
"""
Crea una lista llamada 'dias' con los días de la semana.
Luego imprime el primer y el último elemento de la lista.
"""
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(dias[0])
print(dias[-1])

# Ejercicio 2
"""
Modifica el segundo y el quinto elemento de la lista 'dias' para que estén en inglés.
Imprime la lista modificada.
"""
dias[1] = "Tuesday"
dias[4] = "Friday"
print(dias) 

# Ejercicio 3
"""
Extrae los tres primeros elementos de la lista 'dias' y guárdalos en una nueva lista llamada 'inicio_semana'.
Imprime esa nueva lista.
"""
inicio_semana = dias[:3]
print(inicio_semana)



# Ejercicio 4
"""
Desempaqueta la lista 'dias' en tres variables"""
a,b,c = inicio_semana
a, b,c, _, _, _, _   = dias
print(a)
print(b)
print(c)


# Ejercicio 5
"""
Crea una lista llamada 'numeros' con los números del 1 al 5.
Agrega el número 6 al final de la lista.
Luego imprime la longitud de la lista.
"""
numeros = [1, 2, 3, 4, 5]
list(range(1, 6))

numeros.append(6)
print(numeros)
len(numeros)

# Ejercicio 6
"""
Concatena la lista [8, 9, 10] a la lista 'numeros'.
Imprime la nueva lista.
"""
lista_nueva= [8, 9, 10]
numeros.extend(lista_nueva)
numeros

# Ejercicio 7
"""
Cuenta cuántas veces aparece el número 3 en la lista 'numeros'.
Imprime el resultado.
"""
numeros.count(3)

# Ejercicio 8
"""
Crea una lista anidada con datos de 3 estudiantes: nombre, estatura y peso.
Llama a esta lista 'estudiantes'. Luego imprime la estatura del segundo estudiante.
"""
estudiantes = [["Juan", 1.75, 70], ["María", 1.65, 55], ["Pedro", 1.80, 80]]
estudiantes[1][1]

estudiante1 = {"Nombre": "Juan", "Estatura": 1.75, "Peso": 70}  
estudiante2 = {"Nombre": "María", "Estatura": 1.65, "Peso": 55}
estudiante3 = {"Nombre": "Pedro", "Estatura": 1.80, "Peso": 80}
estudiantes = [estudiante1, estudiante2, estudiante3]
print(estudiantes[1]["Estatura"])  # Imprime la estatura del segundo estudiante


# Ejercicio 9
"""
Usa el método .pop() para eliminar el último elemento de la lista 'numeros'.
Imprime la lista resultante.
"""
numeros.pop()
print(numeros)

# Ejercicio 10
"""
Ordena alfabéticamente la lista 'dias'.
Imprime la lista ordenada.
"""
dias.sort(reverse=True)
print(dias)
# Ejercicio 11

