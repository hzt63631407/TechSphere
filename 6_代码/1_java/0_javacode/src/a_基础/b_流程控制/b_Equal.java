package a_基础.b_流程控制;

public class b_Equal {
    public static void main(String[] args) {

//        String s1 = "1";
//        String s2 = "1";
//        String s3 = s1;
//        System.out.println(s1 == s2);
//        System.out.println(s1.equals(s2));
//        System.out.println(s1 == s3);
//        System.out.println(s1.equals(s3));

//        https://www.cnblogs.com/tinyphp/p/3768214.html

        String s1 = new String("java");
        String s2 = new String("java");
        String s3 = "java";

        System.out.println(s1 == s2);            //false
        System.out.println(s1.equals(s2));    //true
        System.out.println(s1.equals(s3));     //true
        System.out.println(s1 == s3);           //false
    }

}



//在Java中，equals和==都是用于检测两个字符串是否相等，返回类型也都是boolean值，但是二者内部处理却不一样。
//
//==与equals( )
//
//==在Java中是一个二元操作符，用于比较原生类型和对象。当比较基本类型时，较为好理解；
//
//当比较对象时，比较规则是：两个对象基于内存引用，若两个对象的引用完全相同，则==返回的结果为true。
//
//equals( )方法是Object( )类中，根据具体的业务逻辑来定义该方法，用于检查两个对象的相等性。
// 默认是equals方法实现与==操作是一样的，所以在业务中一般都会重写equals( )。
//
//==和equals比较时
//
//1.如果比较基本数据类型（或者说是值变量）
//
//当时Java的基本类型做比较时，应使用 == 比较的是他们的值，而equals是不存在的。
// 因为int float等是基本数据类型，没有equals( )方法，不存在int.equals( )
//
//2.如果比较的是复合数据类型（或者说是引用型变量）
//
//当比较引用型变量时：
//
//==比较的是两个引用是否指向同一个对象实例
//
//equals( )比较看是否被重写，如果有被重写则按照重写的规则比较，没有重写则与==比较规则一样。
