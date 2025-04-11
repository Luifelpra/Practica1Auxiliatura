```mermaid
classDiagram
    class Perro {
        -nombre: String
        -edad: int
        -raza: String
        +hacersonido() String
        +moverse() String
    }

    class Gato {
        -nombre: String
        -color: String
        +hacersonido() String
        +moverse() String
    }

    class Pajaro {
        -nombre: String
        -tipo: String
        +hacersonido() String
        +moverse() String
    }