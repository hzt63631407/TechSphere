package a_基础.e_面向对象.e_面向对象;

//构造方法 Constructor
//
//构造方法可以在new操作时初始化实例对象
//
//构造方法名就是类名
//
//构造方法没有返回值
//
//编译器会为没有定义构造方法的类自动生成默认构造方法
//
//初始化顺序：
//
//初始化字段
//执行构造方法代码
//可以定义多个构造方法，编译器根据参数自动判断使用哪个
//
//   *可以在一个构造方法中通过this()调用另一个构造方法*



// java方法支持链式调用。前一个方法可以作为下一个方法的返回值。


public class a_Constructor {

    public static void main(String[] args) {
        Person ming = new Person("小明", 20);
        System.out.println(ming.getName());

        Person hong = new Person("小红", 12);
        System.out.println(hong.getName());
    }

}

class Person {

    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name.trim();
    }

    public int getAge() {
        return this.age;
    }
}
