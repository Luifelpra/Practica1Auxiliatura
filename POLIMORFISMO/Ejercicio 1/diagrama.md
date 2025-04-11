```mermaid

classDiagram
    class Videojuego {
        -nombre: String
        -plataforma: String
        -cantidadJugadores: int
        +Videojuego(nombre: String, plataforma: String, cantidadJugadores: int)
        +Videojuego(nombre: String)
        +Videojuego(nombre: String, plataforma: String)
        +mostrar(): void
        +agregarJugadores(): void
        +agregarJugadores(cantidad: int): void
    }