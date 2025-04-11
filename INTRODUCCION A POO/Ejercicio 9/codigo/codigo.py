#9. Realiza la abstracción de una Computadora
# a)Muestra los componentes principales de la computadora
# b)Muestra el estado de la computadora (encendido o apagado)
# c)Crea una instancia y simula encender y apagar la computadora.
class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendida = False
        self.componentes = {
            'CPU': 'No especificado',
            'RAM': 'No especificado',
            'Disco Duro': 'No especificado',
            'GPU': 'No especificado',
            'Fuente de Poder': 'No especificado'
        }
    
    def mostrarcomponentes(self):
        print("\nComponentes principales de la computadora:")
        for componente, especificacion in self.componentes.items():
            print(f"- {componente}: {especificacion}")
    
    def mostrarestado(self):
        estado = "ENCENDIDA" if self.encendida else "APAGADA"
        print(f"Estado actual: {estado}")
    
    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("¡Bienvenido! La computadora se está iniciando...")
            print("Sistema operativo cargado correctamente")
        else:
            print("La computadora ya está encendida")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("Guardando configuración...")
            print("La computadora se está apagando...")
            print("¡Hasta pronto!")
        else:
            print("\nLa computadora ya está apagada")
    
    def agregarcomponente(self, nombre, especificaciones):
        self.componentes[nombre] = especificaciones
        print(f"\nComponente actualizado: {nombre} - {especificaciones}")

pc = Computadora("Dell", "XPS 15")

pc.agregarcomponente('CPU', 'Intel Core i7-10750H')
pc.agregarcomponente('RAM', '16GB DDR4 3200MHz')
pc.agregarcomponente('Disco Duro', 'SSD NVMe 1TB')
pc.agregarcomponente('GPU', 'NVIDIA GTX 1650 Ti 4GB')
pc.agregarcomponente('Fuente de Poder', '130W')

pc.mostrarcomponentes()

pc.mostrarestado()

print("Encender")
pc.encender()
pc.mostrarestado()

print("Apagar")
pc.apagar()
pc.mostrarestado()

pc.apagar()