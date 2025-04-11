//3.Sean las siguientes clases que hacen referencia a diferentes tipos de figura:
//  a)Instanciar 1 Cuadrado, 1 Rectángulo y 1 Círculo
//  b)Implementar un método mostrar() en cada clase para imprimir sus dimensiones y área.
//  c)Sobrecargar el método Área para mostrar el área de todas las figuras.
import java.util.ArrayList;
import java.util.List;
abstract class Figura {
    public abstract void mostrar();
    public abstract double area();
}
class Cuadrado extends Figura {
    private double lado;
    public Cuadrado(double lado) {
        this.lado = lado;
    }
    @Override
    public void mostrar() {
        System.out.printf("Cuadrado - Lado: %.2f, Área: %.2f%n", lado, area());
    }
    @Override
    public double area() {
        return lado * lado;
    }
}
class Rectangulo extends Figura {
    private double base;
    private double altura;
    
    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }
    @Override
    public void mostrar() {
        System.out.printf("Rectángulo - Base: %.2f, Altura: %.2f, Área: %.2f%n", 
                         base, altura, area());
    }
    
    @Override
    public double area() {
        return base * altura;
    }
}
class Circulo extends Figura {
    private double radio;
    private static final double PI = Math.PI;
    public Circulo(double radio) {
        this.radio = radio;
    }
    @Override
    public void mostrar() {
        System.out.printf("Círculo - Radio: %.2f, Área: %.2f%n", radio, area());
    }
    @Override
    public double area() {
        return PI * radio * radio;
    }
}

public class Main {
    public static void mostrarAreas(Figura... figuras) {
        for (Figura figura : figuras) {
            System.out.printf("Área de %s: %.2f%n", 
                            figura.getClass().getSimpleName(), 
                            figura.area());
        }
    }
    public static void main(String[] args) {
        Cuadrado cuadrado = new Cuadrado(5);
        Rectangulo rectangulo = new Rectangulo(4, 6);
        Circulo circulo = new Circulo(3);
        cuadrado.mostrar();
        rectangulo.mostrar();
        circulo.mostrar();
        System.out.println("\nMostrando áreas de todas las figuras:");
        mostrarAreas(cuadrado, rectangulo, circulo);
    }
}