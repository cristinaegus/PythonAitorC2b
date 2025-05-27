####################################
# Programación Orientada a Objetos #
####################################
# Creamos una aplicación para gestionar el "Personal" de una empresa

import datetime
#----------------------------------
# Etapa1: Creo una clase "Persona"
#----------------------------------

class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = []

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

print(type(director))
print(type(secretario))

director.presentarse()
secretario.presentarse()

director.trabajando
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

director.viaja("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

secretario = Persona('Juanito', 'Pérez', 'García')#----------------------------------------------------------
# Etapa1: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------
secretario = Persona('Juanito', 'Pérez', 'García')
secretario.ficha()

secretario.fichajes
#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad del tiempo trabajado
#----------------------------------------------------------
from POO.personal import Persona
secretario = Persona('Juanito', 'Pérez', 'García')
secretario.ficha()

secretario.ficha()

secretario.calcula_trabajo()

#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad del sueldo acumulado
#----------------------------------------------------------
from POO.personal import Persona
secretario = Persona('Juanito', 'Pérez', 'García')
secretario.ficha()

secretario.ficha()

secretario.calcula_trabajo()

secretario.calcula_sueldo()


# Crear un método que asigne una dieta de transporte de un euro cada vez que una persona fiche
# Modificar el método que calcula el sueldo para que añada la dieta de transporte.
