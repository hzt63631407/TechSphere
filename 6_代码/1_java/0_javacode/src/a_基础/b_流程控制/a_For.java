package a_基础.b_流程控制;

public class a_For {
    public static void main(String[] args) {
        int[] ns = {1, 4, 9, 16, 25};
        for (int i = 0; i < ns.length; i++) {           // 这个i是角标
            System.out.println(ns[i]);
            }
        for (int n : ns) {
            System.out.println(n);                      // 这个i/n，是里面的元素
        }
    }
}


//for (int n : ns) {
//        //
//        }

//for...each循环可以遍历数组
//
//for...each循环不能指定遍历顺序
//
//for...each循环无法获取计数器