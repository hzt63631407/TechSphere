package a_基础.f_异常;


//NullPointerException即空指针异常，俗称NPE。

//如果一个对象为null，调用其方法或访问其字段就会产生NullPointerException，这个异常通常是由JVM抛出的

public class b_NullPointerException {
    public static void main(String[] args) {
        Person p = new Person();
        System.out.println(p.address.city.toLowerCase());

//        有几种情况
//        a是null；
//        a.b是null；
//        a.b.c是null
//        确定到底是哪个对象是null以前只能打印这样的日志
//        System.out.println(p);
//        System.out.println(p.address);
//        System.out.println(p.address.city);
    }
}

class Person {
    String[] name = new String[2];
    Address address = new Address();
}

class Address {
    String city;
    String street;
    String zipcode;
}



