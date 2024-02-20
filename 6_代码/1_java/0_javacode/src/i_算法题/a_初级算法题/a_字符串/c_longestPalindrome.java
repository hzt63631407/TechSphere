package i_算法题.a_初级算法题.a_字符串;


//leetcode 409
//给定一个包含大写字母和小写字母的字符串 s ，
//返回 通过这些字母构造成的 最长的回文串 。
//在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。

import java.util.HashSet;

public class c_longestPalindrome {
    public int longestPalindrome(String s) {
        HashSet<Character> set = new HashSet<>();
        for(int i = 0 ; i < s.length();i++){
            if(set.contains(s.charAt(i))){
                set.remove(s.charAt(i));
            }else
                set.add(s.charAt(i));
        }
        int res = s.length() - set.size();
        return  set.size() == 0 ? res : res + 1;
    }

}

// todo 为什么不用arraylist