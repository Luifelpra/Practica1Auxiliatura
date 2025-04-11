#5.Crea una clase Estudiante con nombre, nota_1, nota_2
#   a) Agrega un método para calcular el promedio
#   b) Agrega un método para verificar si aprobó (promedio >=6)
#   c) Crea tres estudiantes, muestra sus promedios y si aprobaron
class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2
    
    def calcularpromedio(self):
        return (self.nota_1 + self.nota_2) / 2
    
    def aprobo(self):
        return self.calcularpromedio() >= 6

    def resultado(self):
        promedio = self.calcularpromedio()
        aprob = "APROBADO" if self.aprobo() else "REPROBADO"
        print(f"Estudiante: {self.nombre}")
        print(f"Notas: {self.nota_1}, {self.nota_2}")
        print(f"Promedio: {promedio:.1f} - {aprob}")
        print("----------------------")

estudiante1 = Estudiante("Ana Cortez", 7.5, 8.0)
estudiante2 = Estudiante("Alejandro Bejar", 5.0, 6.5)
estudiante3 = Estudiante("Luis Gómez", 4.0, 3.5)

estudiante1.resultado()
estudiante2.resultado()
estudiante3.resultado()