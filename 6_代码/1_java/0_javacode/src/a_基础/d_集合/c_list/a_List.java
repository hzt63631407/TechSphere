package 集合;


import java.util.List;

public class a_List {
    public static void main(String[] args) {
        //把List变为Array有三种方法
        //List是集合 Array是数组
        //list是列表,list中的元素的数据类型可以不一样。array是数组,数组中的元素的数据类型必须一样
        List<Integer> list = List.of(12, 34, 56);
        Number[] array = list.toArray(new Number[3]);
        for (Number n : array) {
            System.out.println(n);
        }
    }
}




//List的行为和数组几乎完全相同
//通常情况下，我们总是优先使用ArrayList。
//所以我们要始终坚持使用迭代器Iterator来访问List。Iterator本身也是一个对象，但它是由List的实例调用iterator()方法的时候创建的。
//Iterator对象知道如何遍历一个List，并且不同的List类型，返回的Iterator对象实现也是不同的，但总是具有最高的访问效率。
//Iterator对象有两个方法：boolean hasNext()判断是否有下一个元素，E next()返回下一个元素。因此，使用Iterator遍历List代码如下：

