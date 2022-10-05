class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = str(nombre)
        self.nota = int(nota)

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultadoNota(self):
        if 7 <= self.nota <= 10 and self.nota >= 1:
            return "Su calificacion a sido :", self.nota, " por lo tanto esta aprobado"
        elif 7 >= self.nota >= 1:
            return "Su calificacion a sido :", self.nota, " por lo tanto NO esta aprobado"
        else:
            return "El valor de nota ingresado es incorrecto"


alumno1 = Alumno("matias", 8)

alumno2 = Alumno("alicia", 5)
alumno3 = Alumno("marcos", -5)

print(alumno1.resultadoNota())
print(alumno2.resultadoNota())
print(alumno3.resultadoNota())
alumno1.imprimir()
