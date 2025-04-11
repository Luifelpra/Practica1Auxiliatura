#1.Sea la clase Videojuego:
#   a)Instanciar al menos 2 videojuegos
#   b)Sobrecargar el constructor 2 veces
#   c)Implementar un método mostrar()
#   d)Sobrecargar el método agregarJugadores() donde en el primero se agregue solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.
class Videojuego:
    def __init__(self, nombre, plataforma, cantidadjugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadjugadores = cantidadjugadores
    
    @classmethod
    def solonombre(cls, nombre):
        return cls(nombre, "Desconocida", 0)
    
    @classmethod
    def nombreyplataforma(cls, nombre, plataforma):
        return cls(nombre, plataforma, 0)
    
    def mostrar(self):
        print(f"Videojuego: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Jugadores: {self.cantidadjugadores}")
    
    def agregarjugadores(self, cantidad=1):
        if cantidad > 0:
            self.cantidadjugadores += cantidad
        else:
            print("La cantidad debe ser positiva")

juego1 = Videojuego("The Legend of Zelda", "Nintendo Switch", 1)
juego2 = Videojuego.solonombre("Minecraft")

juego1.mostrar()
juego2.mostrar()

juego1.agregarjugadores() 
juego2.agregarjugadores(5) 