package 反射;

import java.lang.reflect.Method;

public class method1 {
    public static void main(String[] args) throws Exception {
        // String对象:
        String s = "Hello world";
        // 获取String substring(int)方法，参数为int:
        Method m = String.class.getMethod("substring", int.class,int.class);
        //自己改变了 使用2个参数为int的方法
        // 在s对象上调用该方法并获取结果:
        String r = (String) m.invoke(s, 6,8); // invoke返回的是object
        // https://blog.csdn.net/u013473691/article/details/52633800
        // 打印调用结果:
        System.out.println(r);
        System.out.println(1);
    }
}
