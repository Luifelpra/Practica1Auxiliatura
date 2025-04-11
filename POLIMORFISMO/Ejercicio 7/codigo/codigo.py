#7.Se hace referencia a algunos animales mediante las siguientes clases:
#   a)Instanciar 1 Perro, 1 Gato y 1 Pájaro.
#   b)Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico.
#   c)Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.).
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    def hacersonido(self):
        return "Guau"
    
    def moverse(self):
        return "Corre"

class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def hacersonido(self):
        return "Miau"
    
    def moverse(self):
        return "Salta"

class Pajaro:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def hacersonido(self):
        return "Pío"
    
    def moverse(self):
        return "Vuela"
perro = Perro("Max", 3, "Labrador")
gato = Gato("Lucy", "Negro")
pajaro = Pajaro("Charly", "Canario")

print(f"Perro: {perro.nombre}")
print(f"Sonido: {perro.hacersonido()}")
print(f"Movimiento: {perro.moverse()}\n")

print(f"Gato: {gato.nombre}")
print(f"Sonido: {gato.hacersonido()}")
print(f"Movimiento: {gato.moverse()}\n")

print(f"Pájaro: {pajaro.nombre}")
print(f"Sonido: {pajaro.hacersonido()}")
print(f"Movimiento: {pajaro.moverse()}")