package a_基础.g_核心类;

// 枚举类是java的一个特殊的类

enum Weekday {
    SUN, MON, TUE, WED, THU, FRI, SAT;
}

public class a_Enum {
    public static void main(String[] args) {
        Weekday day = Weekday.SUN;
        if (day == Weekday.SAT || day == Weekday.SUN) {
            System.out.println("Work at home!");
        } else {
            System.out.println("Work at office!");
        }
    }
}

