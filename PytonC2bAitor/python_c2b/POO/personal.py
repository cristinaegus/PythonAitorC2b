import datetime

class Empleado:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = []
        self.sueldo_hora = sueldo_hora
        self.bono_transporte = 0

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())
        self.bono_transporte += 1

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    def calcula_trabajo(self):
        tiempo_inicial = datetime.timedelta(0)
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        tiempo_trabajado = sum([salida - entrada for entrada, salida in zip(entradas, salidas)], start=tiempo_inicial)
        print(f"Tiempo trabajado: {tiempo_trabajado}")
        return tiempo_trabajado
    
    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.sueldo_hora
        sueldo += self.bono_transporte
        print(f"Sueldo: {sueldo}")
        return sueldo

class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=30):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.coche_empresa = None
        self.gasolina = 0

    def asigna_gasolina(self, litros):
        self.gasolina += litros 
        print(f"Gasolina asignada: {self.gasolina} litros")


class Oficinista(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=20):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.bonus = 0

    def asigna_bonus(self, bonus):
        self.bonus += bonus
        print(f"Bonus asignado: {self.bonus}")

    def calcula_sueldo(self):
        sueldo = super().calcula_sueldo()
        sueldo = sueldo + self.bonus
        return sueldo

class Peon(Empleado):
    pass

# print(__name__)
import time
if __name__ == "__main__":
    director = Directivo('Juan', 'Pérez', 'López')
    secretario = Oficinista('Juanito', 'Pérez', 'García')
    peon = Peon('Pepe', 'Pérez', 'García')

    director.ficha()
    time.sleep(2)
    director.ficha()
    print(director.fichajes)
    #print(director.calcula_trabajo())
    print(director.calcula_sueldo())
    