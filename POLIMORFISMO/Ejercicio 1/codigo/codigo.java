//1.Sea la clase Videojuego:
//  a)Instanciar al menos 2 videojuegos
//  b)Sobrecargar el constructor 2 veces
//  c)Implementar un método mostrar()
//  d)Sobrecargar el método agregarJugadores() donde en el primero se agregue solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.
public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;
    
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }
    
    public Videojuego(String nombre) {
        this(nombre, "Desconocida", 0);
    }
    
    public Videojuego(String nombre, String plataforma) {
        this(nombre, plataforma, 0);
    }
    
    public void mostrar() {
        System.out.println("Videojuego: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Jugadores: " + cantidadJugadores);
    }

    public void agregarJugadores() {
        cantidadJugadores += 1;
    }
    
    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            cantidadJugadores += cantidad;
        } else {
            System.out.println("La cantidad debe ser positiva");
        }
    }
    
    public static void main(String[] args) {
        Videojuego juego1 = new Videojuego("The Legend of Zelda", "Nintendo Switch", 1);
        Videojuego juego2 = new Videojuego("Minecraft");
        juego1.mostrar();
        juego2.mostrar();
        juego1.agregarJugadores();
        juego2.agregarJugadores(5); 
    }
}