import datetime

class Empleado:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.__trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = []
        self.__sueldo_hora = sueldo_hora
        self.bono_transporte = 0

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.__trabajando = not self.__trabajando
        self.fichajes.append(datetime.datetime.now())
        self.bono_transporte += 1
        if self.__trabajando:
            self.imprime_actividades()

    @property
    def sueldo_hora(self):
        print("Estás accediendo al sueldo")
        return self.__sueldo_hora

    @sueldo_hora.setter
    def sueldo_hora(self, nuevo_valor):
        print("Estás modificando el sueldo")
        self.__sueldo_hora += nuevo_valor
        print(f"Nuevo sueldo: {self.__sueldo_hora}")

    def imprime_actividades(self):
        pass

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    def __calcula_trabajo(self):
        tiempo_inicial = datetime.timedelta(0)
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        tiempo_trabajado = sum([salida - entrada for entrada, salida in zip(entradas, salidas)], start=tiempo_inicial)
        print(f"Tiempo trabajado: {tiempo_trabajado}")
        return tiempo_trabajado
    
    def calcula_sueldo(self):
        tiempo_trabajado = self.__calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.__sueldo_hora
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
    
    def imprime_actividades(self):
        print("Actividades del directivo:")
        print("1. Reuniones")
        print("2. Viajes")
        print("3. Presentaciones")
        print("4. Negociaciones")


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
    
    def imprime_actividades(self):  
        print("Actividades del oficinista:")
        print("1. Reuniones")
        print("2. Llamadas telefónicas")
        print("3. Correos electrónicos")
        print("4. Gestión de documentos")

class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.guardias = 0

    def ficha(self):
        super().ficha()
        if self._Empleado__trabajando:
            if self.fichajes[-1].hour > 21 or self.fichajes[-1].hour < 11:
                self.guardias += 1
                print("Guardia nocturna asignada")

    def calcula_sueldo(self):
        sueldo = super().calcula_sueldo()
        sueldo = sueldo + self.guardias * 10
        return sueldo
    
    def imprime_actividades(self):  
        print("Actividades del peón")
        print("1. Limpieza")
        print("2. Operar con la máquina")
        print("3. Mantenimiento de instalaciones")
        print("4. Seguridad")
    

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
    
