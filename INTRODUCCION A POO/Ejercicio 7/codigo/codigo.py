#7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
# a)Crea un método para instalar una nueva aplicación
# b)Crea un método para utilizar una aplicación (las aplicaciones que pesan más de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza un 1% cada 10 minutos de uso)
# c)Muestra el porcentaje de batería restante
# d)Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el mensaje de celular apagado
class Celular:
    def __init__(self):
        self.bateria = 100
        self.espaciototal = 1024
        self.espacioocupado = 0
        self.aplicaciones = {}
    
    def instalaraplicacion(self, nombre, tamaño):
        if self.espacioocupado + tamaño > self.espaciototal:
            print(f"No hay espacio suficiente para instalar {nombre}")
            return False
        if len(self.aplicaciones) >= 20:
            print("Límite de aplicaciones alcanzado (20)")
            return False
        if nombre in self.aplicaciones:
            print(f"La aplicación {nombre} ya está instalada")
            return False
            
        self.aplicaciones[nombre] = tamaño
        self.espacioocupado += tamaño
        print(f"Aplicación {nombre} instalada correctamente")
        return True
    
    def usaraplicacion(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado (batería agotada)")
            return False
        if nombre not in self.aplicaciones:
            print(f"La aplicación {nombre} no está instalada")
            return False
        tamaño = self.aplicaciones[nombre]
        min10 = minutos / 10
        if tamaño > 250:
            consumo = min10 * 5
        elif tamaño > 100:
            consumo = min10 * 2
        else:
            consumo = min10 * 1
            
        if self.bateria - consumo <= 0:
            self.bateria = 0
            print("Celular apagado (batería agotada durante el uso)")
            return False 
        self.bateria -= consumo
        print(f"Usando {nombre} por {minutos} minutos. Batería consumida: {consumo:.1f}%")
        return True
    def mostrarbateria(self):
        print(f"Batería restante: {self.bateria:.1f}%")
    def mostrarespacio(self):
        print(f"Espacio usado: {self.espacioocupado}MB de {self.espaciototal}MB")
        print(f"Aplicaciones instaladas: {len(self.aplicaciones)}/20")
celular = Celular()

celular.instalaraplicacion("WhatsApp", 80)
celular.instalaraplicacion("Instagram", 150)
celular.instalaraplicacion("Juego Pesado", 300)

celular.mostrarespacio()
celular.mostrarbateria()
print("\n")


celular.usaraplicacion("WhatsApp", 30) 
celular.usaraplicacion("Instagram", 50)
celular.usaraplicacion("Instagram", 280)
celular.mostrarbateria()
print("\n")

celular.usaraplicacion("Juego Pesado", 60) 
celular.mostrarbateria()

celular.usaraplicacion("WhatsApp", 10)