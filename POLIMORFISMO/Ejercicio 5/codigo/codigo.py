#5.Se hace referencia a algunos de los diferentes ambientes de la Universidad mediante las siguientes clases:
#   a)Instanciar 2 objetos Oficina, 2 Aulas y 1 Laboratorio
#   b)Crear un método mostrar() para mostrar los datos de cada objeto
#   c)Sobrecargar el método cantidadMuebles(), para conocer el número total de muebles dentro de cada ambiente
class Oficina:
    def __init__(self, nrosillas, nroescritorios, nroestanterias):
        self.nrosillas = nrosillas
        self.nroescritorios = nroescritorios
        self.nroestanterias = nroestanterias
    
    def mostrar(self):
        print("Oficina:")
        print(f"  - Sillas: {self.nrosillas}")
        print(f"  - Escritorios: {self.nroescritorios}")
        print(f"  - Estanterías: {self.nroestanterias}")
    
    def cantidadmuebles(self, incluirestanterias=True):
        if incluirestanterias:
            return self.nrosillas + self.nroescritorios + self.nroestanterias
        else:
            return self.nrosillas + self.nroescritorios

class Aula:
    def __init__(self, nombre, capacidad, nropupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nropupitres = nropupitres
    
    def mostrar(self):
        print("Aula:")
        print(f"  - Nombre: {self.nombre}")
        print(f"  - Capacidad: {self.capacidad} personas")
        print(f"  - Pupitres: {self.nropupitres}")
    
    def cantidadmuebles(self, incluirsillasextra=False, sillasextra=0):
        if incluirsillasextra:
            return self.nropupitres + sillasextra
        else:
            return self.nropupitres

class Laboratorio:
    def __init__(self, nombre, capacidad, nromesas, nrosillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nromesas = nromesas
        self.nrosillas = nrosillas
    
    def mostrar(self):
        print("Laboratorio:")
        print(f"  - Nombre: {self.nombre}")
        print(f"  - Capacidad: {self.capacidad} personas")
        print(f"  - Mesas: {self.nromesas}")
        print(f"  - Sillas: {self.nrosillas}")
    
    def cantidadmuebles(self, solomesas=False):
        if solomesas:
            return self.nromesas
        else:
            return self.nromesas + self.nrosillas

oficina1 = Oficina(4, 2, 3)
oficina2 = Oficina(6, 3, 5)
aula1 = Aula("Aula 101", 30, 15)
aula2 = Aula("Aula 202", 25, 20)
laboratorio = Laboratorio("Lab de Computación", 20, 10, 20)

print("=== Mostrar ===")
oficina1.mostrar()
oficina2.mostrar()
aula1.mostrar()
aula2.mostrar()
laboratorio.mostrar()

print("\n=== Muebles ===")
print(f"Oficina 1 - Total muebles: {oficina1.cantidadmuebles()}")
print(f"Oficina 1 - Sin estanterías: {oficina1.cantidadmuebles(incluirestanterias=False)}")
print(f"Aula 1 - Pupitres: {aula1.cantidadmuebles()}")
print(f"Aula 1 - Pupitres + 5 sillas extra: {aula1.cantidadmuebles(incluirsillasextra=True, sillasextra=5)}")
print(f"Laboratorio - Total muebles: {laboratorio.cantidadmuebles()}")
print(f"Laboratorio - Solo mesas: {laboratorio.cantidadmuebles(solomesas=True)}")