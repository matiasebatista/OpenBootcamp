class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__("rojo", 4, 4)


nuevoCoche = Coche(100, 1000)
print(nuevoCoche.color)
print(nuevoCoche.cilindrada)
print(nuevoCoche.puertas)
