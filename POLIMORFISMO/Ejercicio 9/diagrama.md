```mermaid
classDiagram
    class BloqueCofre {
        -capacidad: int
        -resistencia: int
        -tipo: String
        +accion() String
        +colocar(orientacion: String) String
        +romper() String
    }

    class BloqueTnt {
        -tipo: String
        -daño: int
        +accion() String
        +colocar(orientacion: String) String
        +romper() String
    }

    class BloqueHorno {
        -color: String
        -capacidadComida: int
        +accion() String
        +colocar(orientacion: String) String
        +romper() String
    }