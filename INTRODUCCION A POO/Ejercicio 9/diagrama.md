```mermaid
classDiagram
    class Computadora {
        -marca: str
        -modelo: str
        -encendida: bool
        -componentes: dict
        +Computadora(marca: str, modelo: str)
        +encender() void
        +apagar() void
        +agregarcomponente(nombre: str, especificaciones: str) void
        +mostrarcomponentes() void
        +mostrarestado() void
    }