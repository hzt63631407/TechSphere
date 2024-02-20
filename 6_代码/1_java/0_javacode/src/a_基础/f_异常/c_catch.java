package a_基础.f_异常;

public class c_catch {
    public static void main(String[] args) {
        System.out.println("1");
        try {
            process1();
        } catch (Exception e) {
            e.printStackTrace();
//            System.out.println("2");
        }
    }

    static void process1() {
        process2();
    }

    static void process2() {
        Integer.parseInt(null); // 会抛出NumberFormatException
    }
}


