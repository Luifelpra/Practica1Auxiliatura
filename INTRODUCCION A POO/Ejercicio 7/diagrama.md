```mermaid
classDiagram
    class Celular {
        -bateria: int
        -espaciototal: int
        -espacioocupado: int
        -aplicaciones: dict
        +Celular()
        +instalaraplicacion(nombre: str, tamaño: int) bool
        +usaraplicacion(nombre: str, minutos: int) bool
        +mostrarbateria() void
        +mostrarespacio() void
    }