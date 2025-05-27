
def area(radio):
    return 3.141592653589793 * radio ** 2
def perimetro(radio):
    return 2 * 3.141592653589793 * radio


if __name__ == "__main__":
    # Si el archivo se ejecuta directamente, se ejecuta este bloque
    # Si se importa, no se ejecuta
    print("Ejecutando el módulo circulo")
    print(area(25))
    print(perimetro(35))