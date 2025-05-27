class Coche:
    ruedas = 4
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
        self.puertas = 4

    def __str__(self):
        return f"{self.marca} {self.modelo}"

    def __del__(self):
        print(f"Se ha eliminado el coche {self}")
    
    def presentarse(self):
        print(f"Hola soy un coche {self.marca} {self.modelo}")

    def __len__(self):
        return int(self.longitud*100)

    def __gt__(self, otro):
        return self.precio > otro.precio
    
    def __eq__(self, otro):
        return self.precio == otro.precio