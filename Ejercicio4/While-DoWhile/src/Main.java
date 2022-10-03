public class Main {
    public static void main(String[] args) {
        funcWhile(1);
        funcDoWhile(2);
        funcFor(2);
        funcSwitch("INVIERNO");
        funcSwitch("dia");
    }
    public static void funcWhile(int number){
        while (number<3){
            System.out.println(number);
            number+=1;
        }
    }
    public static void funcDoWhile(int number2){
        do{
            System.out.println(number2);
            number2+=1;
        }while(number2<3);
    }
    public static void funcFor(int number3){
        for(number3 = number3;number3 <= 3;number3 ++){
            System.out.println(number3);
        }
    }

    public static void funcSwitch(String string){
        switch (string) {
            case "VERANO" -> System.out.println("es VERANO");
            case "INVIERNO" -> System.out.println("es INVIERNO");
            case "OTOÑO" -> System.out.println("es OTOÑO");
            case "PRIMAVERA" -> System.out.println("es PRIMAVERA");
            default -> System.out.println(string + " no es una estacion");
        }
    }
}