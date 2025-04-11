//5.Crea una clase Estudiante con nombre, nota_1, nota_2
//  a) Agrega un método para calcular el promedio
//  b) Agrega un método para verificar si aprobó (promedio >=6)
//  c) Crea tres estudiantes, muestra sus promedios y si aprobaron
public class Estudiante {
    private String nombre;
    private double nota1;
    private double nota2;
    public Estudiante(String nombre, double nota1, double nota2) {
        this.nombre = nombre;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }
    public double calcularPromedio() {
        return (nota1 + nota2) / 2;
    }
    public boolean aprobo() {
        return calcularPromedio() >= 6;
    }
    public void mostrarResultados() {
        double promedio = calcularPromedio();
        String estado = aprobo() ? "APROBADO" : "REPROBADO";
        System.out.println("Estudiante: " + nombre);
        System.out.printf("Notas: %.1f, %.1f%n", nota1, nota2);
        System.out.printf("Promedio: %.1f - %s%n", promedio, estado);
        System.out.println("----------------------");
    }
    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("Ana Cortez", 7.5, 8.0);
        Estudiante estudiante2 = new Estudiante("Alejandro Bejar", 5.0, 6.5);
        Estudiante estudiante3 = new Estudiante("Luis Gomez", 4.0, 3.5);
        
        estudiante1.mostrarResultados();
        estudiante2.mostrarResultados();
        estudiante3.mostrarResultados();
    }
}