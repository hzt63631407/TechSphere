package 反射;

//通过Class实例获取class信息的方法称为反射（Reflection）；

//有一个Class类 创建其他类时，Class类就会创建一个对应的实例

//以String类为例，当JVM加载String类时，它首先读取String.class文件到内存，然后，为String类创建一个Class实例并关联起来：
//
//Class cls = new Class(String);

import java.lang.reflect.Field;

public class class1 {
    public static void main(String[] args) throws Exception {
        Person p = new Person("Xiao Ming");
        System.out.println(p.getName()); // "Xiao Ming"
        Class c = p.getClass();
        Field f = c.getDeclaredField("name");
        f.setAccessible(true);
//        Object value = f.get(p);
//        System.out.println(value);
        f.set(p, "Xiao Hong");
        System.out.println(p.getName()); // "Xiao Hong"
    }
}

class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}

