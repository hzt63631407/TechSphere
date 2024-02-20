package 面向对象;

/*
对象的多态性。

class 猫 extends 动物
()
class 狗 extends 动物
()

猫 x = new 猫();
动物 x = new 猫();

猫这类事物既具备着猫的形态，又具备着动物的形态。
这就是对象的多态性。

简单说：就是一个对象对应着不同的类型。

多态在代码中的体现：
父类或者接口的引用指向其子类的对象。

多态的好处，
提高了代码的扩展性，前期定义的代码可以使用后期的内容。

多态的弊端：
前期定义的内容不能使用（调用）后期子类的特有内容。

多态的前提：
1.必须有关系。继承，实现。
2.要有覆盖。
*/


abstract class Animal {
    abstract void eat();
}

class Dog extends Animal {
    void eat() {
        System.out.println("啃骨头");
    }

    void lookhome() {
        System.out.println("看家");
    }
}

class Cat extends Animal {
    void eat() {
        System.out.println("吃鱼");
    }

    void catchMouse() {
        System.out.println("捉老鼠");
    }
}

class Pig extends Animal {
    void eat() {
        System.out.println("饲料");
    }

    void gongdi() {
        System.out.println("拱地");
    }

}

public class b_DuoTaiDemo {
    public static void main(String[] args) {
		/*
		Cat c =new Cat();
		Dog d =new Dog();
		method(c);
		method(d);
		method(new Pig());
		*/
        Animal a = new Cat();   //自动类型提升，猫对象提升了动物类型。但是特有功能无法访问。
        //作用就是限制对特有功能的访问。
        //专业术语：向上转型。将子类型隐藏，就不用使用子类的特有方法。

        a.eat();
        //如果还想用具体动物猫的特有功能。
        //你可以将对象进行向下转型。
//		Cat c=(Cat)a;   //向下转型的目的是为了使用子类中的特有方法。
//		c.eat();
//		c.catchMouse();
        method(new Dog());


//		# 注意：对于转型，自始至终都是子类对象在做着类型的变化。
//		Animal a1 =new Dog();
//		Cat c1=(Cat)a1;//java.lang.ClassCastException:类型转换异常

    }

    public static void method(Animal a) //Animal a =new Dog()
    {
        a.eat();
        if (a instanceof Cat)  //instenceof ，用于判断对象的具体类型，只能用于引用数据类型判断
        //通常在向下转型前用于健壮性的判断
        {
            Cat c = (Cat) a;
            c.catchMouse();
        } else {
            System.out.println("不是猫");
        }
        // a.catchMouse();
    }

	/*public static void method(Cat c)
	{
		c.eat();
	}
	public static void method(Dog d)
	{
		d.eat();
	}
    */
}


