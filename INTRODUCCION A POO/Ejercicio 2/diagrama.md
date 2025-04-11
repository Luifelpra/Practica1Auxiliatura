```mermaid
classDiagram
    class Empleado {
        -nombre: String
        -sueldo: float
        +Empleado(nombre: String, sueldo: float)
        +calcular_sueldo_anual() float
        +aplicar_aumento() void
        +mostrar_datos() void
    }