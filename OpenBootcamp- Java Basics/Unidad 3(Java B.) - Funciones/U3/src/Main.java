public class Main {
    public static void main(String[] args) {
        System.out.println(cuentaImpuesto(125));


    }

    public static double cuentaImpuesto(int numero){
        double i = 1.21;
        return numero*i;
    }
}