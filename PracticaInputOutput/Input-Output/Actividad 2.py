import pickle
class Vehiculo:

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def getVehiculo(self):
        return f'El auto es marca {self.marca} y es de color {self.color}'


Auto1 = Vehiculo("Renault", "Rojo")
print(Auto1.getVehiculo())
file = open('fichero.txt','w+')
file.write(Auto1.getVehiculo())
file.close()
