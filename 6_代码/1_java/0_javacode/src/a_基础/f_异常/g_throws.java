package a_基础.f_异常;


//  使用throws关键字声明的方法表示此方法不处理异常（除数是0等），而交给方法调用处进行处理。

public class g_throws {
    public static int divideNum(int m, int n) throws ArithmeticException  {
        // 声明了异常，可能会抛出，由调用者决定是否处理，如果不声明，但是还是catch了，还是可以运行

        int div = m / n;
        return div;
    }

    public static void main(String[] args) {

        g_throws obj = new g_throws();
        try {
            System.out.println(obj.divideNum(45, 0));
        } catch (ArithmeticException e) {
            System.out.println("Number cannot be divided by 0");
        }
        System.out.println("Rest of the code..");
    }
}
