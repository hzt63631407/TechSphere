package a_数据类型.b_引用数据类型;

// 字符串类型String是引用类型

//1.s.length(),求长度
//2.s.charAt(i),第几个坐标
//2.s.indexOf(l),l第一个出现的坐标

public class b_String {
    public static void main(String[] args) {
        String s = "Hello";
        System.out.println(s.length());
        String t = s;
        System.out.println(t.charAt(2));
        s = "hello";
        System.out.println(s);
    }
}
