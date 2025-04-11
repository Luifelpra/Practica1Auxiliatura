```` mermaid
classDiagram
    class Figura {
        <<abstract>>
        +mostrar()* void
        +area()* double
    }
    
    class Cuadrado {
        -lado: double
        +mostrar() void
        +area() double
    }
    
    class Rectangulo {
        -base: double
        -altura: double
        +mostrar() void
        +area() double
    }
    
    class Circulo {
        -radio: double
        +mostrar() void
        +area() double
    }
    
    Figura <|-- Cuadrado
    Figura <|-- Rectangulo
    Figura <|-- Circulo