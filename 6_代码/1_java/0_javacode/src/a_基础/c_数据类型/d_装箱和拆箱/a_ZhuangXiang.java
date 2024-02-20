package a_基础.c_数据类型.d_装箱和拆箱;

//基本类型与包装类型的异同：
//
//1、在Java中，一切皆对象，但八大基本类型却不是对象。
//
//2、声明方式的不同，基本类型无需通过new关键字来创建，而包装类型需new关键字。
//
//3、存储方式及位置的不同，基本类型是直接存储变量的值保存在堆栈中能高效的存取，
// 包装类型需要通过引用指向实例，具体的实例保存在堆中。
//
//4、初始值的不同，包装类型的初始值为null，基本类型的的初始值视具体的类型而定，
// 比如int类型的初始值为0，boolean类型为false；（0分和没参加考试）
//
//5、使用方式的不同，比如与集合类合作使用时只能使用包装类型。
//
//6、什么时候该用包装类，什么时候用基本类型，看基本的业务来定：这个字段允不允许null值，如果允许null值，则必然要用包装类，
//   否则值类型就可以了，用到比如泛型和反射调用函数.，就需要用包装类

//1、集合类泛型只能是包装类；
//
//// 编译报错
//   List<int> list1 = new ArrayList<>();
//
//// 正常
//   List<Integer> list2 = new ArrayList<>();
//
//https://www.php.cn/java-article-410108.html

//https://cloud.tencent.com/developer/article/1362754


public class a_ZhuangXiang {
    public static void main(String[] args) {
        int i = 100;
        // 通过new操作符创建Integer实例(不推荐使用,会有编译警告):
        Integer n1 = new Integer(i);
        // 通过静态方法valueOf(int)创建Integer实例:
        Integer n2 = Integer.valueOf(i);
        // 通过静态方法valueOf(String)创建Integer实例:
        Integer n3 = Integer.valueOf("100");
        System.out.println(n3.intValue());
    }


}
