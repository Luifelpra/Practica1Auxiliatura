public class Persona {
     private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }
    

    public void saludar() {
        System.out.println("Hola, soy " + nombre + " de " + ciudad);
    }
    
     public boolean esMayorDeEdad() {
        return self.edad>=18:
    }
    
}

public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 25, "La Paz ");
        Persona persona2 = new Persona("María", 17, "Santa Cruz");
        Persona persona3 = new Persona("Carlos", 30, "Cochabamba");
        
        persona1.saludar();
        persona2.saludar();
        persona3.saludar();
        
        System.out.println(persona1.getNombre() + " es mayor de edad: " + persona1.esMayorDeEdad());
        System.out.println(persona2.getNombre() + " es mayor de edad: " + persona2.esMayorDeEdad());
        System.out.println(persona3.getNombre() + " es mayor de edad: " + persona3.esMayorDeEdad());
    }
}