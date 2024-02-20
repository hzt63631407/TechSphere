package a_基础.c_数据类型.c_引用数据类型;

//数组是引用类型，数组的大小是不可变的
//里面的类型相同，有序
//数组元素可以是值类型（如int）或引用类型（如String），但数组本身是引用类型；


//1.访问某一个：ns[0]
//2.全部输出：Arrays.toString(ns)
//3.求长度：ns.length
//4.没有add方法

import java.util.Arrays;

public class a_Array {
    public static void main(String[] args) {
        int[] ns = new int[5];
        String[] ss = new String[5];
        String[] st = {"r", "he"};
        System.out.println(ns);
        System.out.println(ns[0]);
        System.out.println(st[1]);

        int[] ns1 = { 1, 1, 2, 3, 5, 8 };
        System.out.println(ns1); // 类似 [I@7852e922
        System.out.println(Arrays.toString(ns1));

    }
}
