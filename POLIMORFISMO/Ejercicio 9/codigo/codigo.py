#9.Para los bloques del juego Minecraft se usará los siguientes objetos:
#   a)Crear e instanciar al menos 2 bloques de cada tipo
#   b)Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque.
#   c)Sobrecarga colocar() para permitir colocar un bloque en diferentes orientaciones (por ejemplo, en el suelo o en la pared).
#   d)Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque y que puede suceder al romperlos.
class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo="Roble"):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo
    
    def accion(self):
        return f"Abriendo cofre de {self.tipo} (Capacidad: {self.capacidad} slots)"
    
    def colocar(self, orientacion="suelo"):
        if orientacion == "suelo":
            return f"Cofre colocado en el suelo (Resistencia: {self.resistencia})"
        elif orientacion == "pared":
            return f"Cofre colocado en la pared (Resistencia: {self.resistencia})"
        else:
            return f"Cofre colocado en posición {orientacion}"
    
    def romper(self):
        return f"¡Cuidado! Rompiendo cofre de {self.tipo}. Puede contener items."

class BloqueTnt:
    def __init__(self, tipo="Normal", daño=4):
        self.tipo = tipo
        self.daño = daño
    
    def accion(self):
        return f"¡{self.tipo} TNT activada! (Daño: {self.daño} corazones)"
    
    def colocar(self, orientacion="suelo"):
        if orientacion == "suelo":
            return "TNT colocada en el suelo (¡Peligro!)"
        elif orientacion == "pared":
            return "TNT colocada en la pared (¡Explosión vertical!)"
        else:
            return f"TNT colocada en posición {orientacion}"
    
    def romper(self):
        return "¡BOOM! La TNT ha explotado al romperla."

class BloqueHorno:
    def __init__(self, color="Gris", capacidadComida=3):
        self.color = color
        self.capacidadComida = capacidadComida
    
    def accion(self):
        return f"Horno {self.color} encendido (Cocina {self.capacidadComida} items)"
    
    def colocar(self, orientacion="suelo"):
        if orientacion == "suelo":
            return f"Horno {self.color} colocado en el suelo"
        elif orientacion == "pared":
            return f"Horno {self.color} colocado en la pared"
        else:
            return f"Horno colocado en posición {orientacion}"
    
    def romper(self):
        return f"Rompiendo horno {self.color}. ¡Cuidado con los items cocinados!"
cofre1 = BloqueCofre(27, 15, "Roble")
cofre2 = BloqueCofre(54, 30, "End")

tnt1 = BloqueTnt("Normal", 4)
tnt2 = BloqueTnt("Super", 8)

horno1 = BloqueHorno("Gris", 3)
horno2 = BloqueHorno("Negro", 5)

print("=== Accion ===")
print(f"Cofre 1: {cofre1.accion()}")
print(f"TNT 1: {tnt1.accion()}")
print(f"Horno 1: {horno1.accion()}\n")

print("=== Colocar ===")
print(f"Cofre 2: {cofre2.colocar('pared')}")
print(f"TNT 2: {tnt2.colocar('suelo')}")
print(f"Horno 2: {horno2.colocar('techo')}\n")


print("=== Romper ===")
print(f"Cofre 1: {cofre1.romper()}")
print(f"TNT 2: {tnt2.romper()}")
print(f"Horno 2: {horno2.romper()}")