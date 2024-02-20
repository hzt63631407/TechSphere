package 泛型;

public class a_Fan {
    public static void main(String[] args) {
        Pair<String> p1 = new Pair <>("Hello", "world");
        // 集合里面只能放一个或多个string的类型 是可变的     数组是不可变的
        Pair<Integer> p2 = new Pair <>(123, 456);
        Class c1 = p1.getClass();
        Class c2 = p2.getClass();
        System.out.println(c1==c2); // true
        System.out.println(c1==Pair.class); // true

    }

}
class Pair<T> {
    private T first;
    private T last;
    public Pair(T first, T last) {
        this.first = first;
        this.last = last;
    }
    public T getFirst() {
        return first;
    }
    public T getLast() {
        return last;
    }
}


//// 创建可以存储String的ArrayList:
//ArrayList<String> strList = new ArrayList<String>();
//// 创建可以存储Float的ArrayList:
//ArrayList<Float> floatList = new ArrayList<Float>();
//// 创建可以存储Person的ArrayList:
//ArrayList<Person> personList = new ArrayList<Person>();

//// 无编译器警告:
//List<String> list = new ArrayList<String>();
//list.add("Hello");
//list.add("World");
//// 无强制转型:
//String first = list.get(0);
//String second = list.get(1);