package a_基础知识;
import java.util.Scanner;

public class f_Input {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input your name: ");
        String name = scanner.nextLine();
        System.out.print("Input your age: ");
        int age = scanner.nextInt();
        System.out.println("Hi, " + name + ", you are " + age);
    }

}
