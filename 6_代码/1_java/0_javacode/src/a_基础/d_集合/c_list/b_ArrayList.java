package c_集合.b_list;

import java.util.ArrayList;

import java.util.List;

public class b_ArrayList {
    public static void main(String[] args) {
        List<String> sites = new ArrayList<String>();           // todo
//      List<String> sites = new List<String>() java: java.util.List是抽象的; 无法实例化
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Weibo");
        sites.set(2, "Wiki"); // 第一个参数为索引位置，第二个为要修改的值
        System.out.println(sites);
        for (int i = 0; i < sites.size(); i++) {
            System.out.println(sites.get(i));
        }
        System.out.println(sites.get(1));
    }
}


// https://blog.csdn.net/qq_42514371/article/details/114841201
// https://blog.csdn.net/qq_31655965/article/details/54746235