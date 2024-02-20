package 反射;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

public class DongTaiDaiLi {
    public static void main(String[] args) {
        InvocationHandler handler = new InvocationHandler() {
//            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                System.out.println(method);
                if (method.getName().equals("morning")) {
                    System.out.println("Good morning, " + args[0]);
                }
                return null;
            }
        };
        Hello hello = (Hello) Proxy.newProxyInstance(
                Hello.class.getClassLoader(), // 传入ClassLoader
                new Class[] { Hello.class }, // 传入要实现的接口                new 类名(){方法定义} 这种写法是匿名内部类。
                handler); // 传入处理调用方法的InvocationHandler          https://zhidao.baidu.com/question/401096048.html
        hello.morning("Bob");                              // https://blog.csdn.net/qq_41703539/article/details/80345712
    }
}

interface Hello {
    void morning(String name);
}

