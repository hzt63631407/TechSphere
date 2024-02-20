package a_基础知识;

import java.util.Scanner;

// 尽量少用switch

public class e_Switch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Select 1 ~ 4: ");
        int opt = scanner.nextInt();
        switch (opt) {
            case 1:
                System.out.println("Selected 1");
                break;
            case 2:                     // switch 具有穿透性
                System.out.println("Selected 2");
            case 3:
                System.out.println("Selected 2,3");
                break;
            case 4:
                System.out.println("Selected 4");
                break;
            default:
                System.out.println("Not selected.");
        }
        System.out.println("END");
    }
}
