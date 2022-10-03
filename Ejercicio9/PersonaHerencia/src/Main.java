public class Main {
    public static void main(String[] args) {

    Persona persona = new Persona();
        persona.setEdad(25);
        persona.setNombre("Matias");
        persona.setTelefono("9812314224");
        System.out.println(persona.getEdad());
        System.out.println(persona.getNombre());
        System.out.println(persona.getTelefono());
    Cliente cliente = new Cliente();
        cliente.setNombre("Jorge");
        cliente.setEdad(19);
        cliente.setTelefono("123456789");
        cliente.setCredito(2000);
        System.out.println(cliente.getEdad());
        System.out.println(cliente.getNombre());
        System.out.println(cliente.getTelefono());
        System.out.println(cliente.getCredito());
    Trabajador trabajador = new Trabajador();
        trabajador.setNombre("Maria");
        trabajador.setEdad(20);
        trabajador.setTelefono("14123241");
        trabajador.setSalario(300000);
        System.out.println(trabajador.getEdad());
        System.out.println(trabajador.getNombre());
        System.out.println(trabajador.getTelefono());
        System.out.println(trabajador.getSalario());
}

}

class Persona{
    private int edad;
    private String nombre;
    private String telefono;

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }
    public void setTelefono(String telefono){
        this.telefono = telefono;
    }
    public String getTelefono(){
        return this.telefono;
    }

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }
}

class Cliente extends Persona{
    private int credito;

    public void setCredito(int credito){
        this.credito = credito;
    }
    public int getCredito(){
        return this.credito;
    }
}
class Trabajador extends Persona{
    private int salario;

    public void setSalario(int salario){
        this.salario = salario;
    }
    public int getSalario(){
        return this.salario;
    }
}