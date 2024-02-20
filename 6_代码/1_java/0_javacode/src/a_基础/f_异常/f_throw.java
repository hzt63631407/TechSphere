package a_基础.f_异常;

public class f_throw {
    public static void checkNegativeNum(int num) {
        if (num < 0) {
            throw new ArithmeticException("不能输入负数！");   // 如果非法抛出异常
        } else {
            System.out.println("输入的数字是：" + num + "，合法！");
        }

    }

    public static void main(String[] args) {
        f_throw obj = new f_throw();
        obj.checkNegativeNum(-3);
    }
}


// Exception in thread "main" java.lang.ArithmeticException: 不能输入负数！
//    at TestThrow.checkNegativeNum(TestThrow.java:7)
//    at TestThrow.main(TestThrow.java:15)