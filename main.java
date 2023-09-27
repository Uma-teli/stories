import java.util.*;  
class main{

         public static void main(String[] args) {

            System.out.println("Hello, World!"); 
            Scanner sc= new Scanner(System.in);    //System.in is a standard input stream  
            System.out.print("Enter first number- ");  
            int a= sc.nextInt();  
            System.out.print("Enter second number- ");  
            int b= sc.nextInt();  
            int res;
            res= a+b;
            System.out.println("result is " +res); 
            System.out.println(res.getClass().getSimpleName());



}
}