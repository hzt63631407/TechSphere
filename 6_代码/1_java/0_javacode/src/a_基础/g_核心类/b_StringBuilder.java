package 核心类;


//为了能高效拼接字符串，Java标准库提供了StringBuilder，它是一个可变对象，可以预分配缓冲区，
// 这样，往StringBuilder中新增字符时，不会创建新的临时对象：

public class b_StringBuilder {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder(1024);
        sb.append("Mr ")
                .append("Bob")
                .append("!")
                .insert(0, "Hello, ");
        System.out.println(sb.toString());
    }


}


