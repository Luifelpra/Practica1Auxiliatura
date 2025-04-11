#3.Sean las siguientes clases que hacen referencia a diferentes tipos de figura:
#   a)Instanciar 1 Cuadrado, 1 Rectángulo y 1 Círculo
#   b)Implementar un método mostrar() en cada clase para imprimir sus dimensiones y área.
#   c)Sobrecargar el método Área para mostrar el área de todas las figuras.
import math
class Figura:
    def mostrar(self):
        pass
    
    def area(self):
        pass
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def mostrar(self):
        print(f"Cuadrado - Lado: {self.lado}, Área: {self.area()}")
    
    def area(self):
        return self.lado ** 2
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mostrar(self):
        print(f"Rectángulo - Base: {self.base}, Altura: {self.altura}, Área: {self.area()}")
    
    def area(self):
        return self.base * self.altura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def mostrar(self):
        print(f"Círculo - Radio: {self.radio}, Área: {self.area():.2f}")
    
    def area(self):
        return math.pi * (self.radio ** 2)

def mostrarareas(*figuras):
    for figura in figuras:
        print(f"Área de {figura.__class__.__name__}: {figura.area():.2f}")

cuadrado = Cuadrado(5)
rectangulo = Rectangulo(4, 6)
circulo = Circulo(3)

cuadrado.mostrar()
rectangulo.mostrar()
circulo.mostrar()

print("\nMostrando áreas de todas las figuras:")
mostrarareas(cuadrado, rectangulo, circulo)