```mermaid
classDiagram
    class Oficina {
        -nrosillas: int
        -nroescritorios: int
        -nroestanterias: int
        +mostrar() void
        +cantidadmuebles(incluirestanterias: bool) int
    }

    class Aula {
        -nombre: str
        -capacidad: int
        -nropupitres: int
        +mostrar() void
        +cantidadmuebles(incluirsillasextra: bool, sillasextra: int) int
    }

    class Laboratorio {
        -nombre: str
        -capacidad: int
        -nromesas: int
        -nrosillas: int
        +mostrar() void
        +cantidadmuebles(solomesas: bool) int
    }