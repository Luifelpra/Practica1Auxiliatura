```mermaid
classDiagram
    class Estudiante {
        -nombre: String
        -nota_1: float
        -nota_2: float
        +Estudiante(nombre: String, nota_1: float, nota_2: float)
        +calcular_promedio() float
        +aprobo() boolean
        +mostrar_resultados() void
    }