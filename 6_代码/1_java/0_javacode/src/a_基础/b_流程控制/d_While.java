package a_基础知识;

public class d_While {

    public static void main(String[] args) {
        int sum = 0;
        int n = 1;
        // while 可能一次都不执行
        while (n < 10) {
            sum = sum + n;
            n++;
        }
        System.out.println(n);
        System.out.println(sum);
    }

}
