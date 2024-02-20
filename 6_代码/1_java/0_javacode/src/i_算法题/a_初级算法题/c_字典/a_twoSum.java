package i_算法题.a_初级算法题.c_字典;




import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;


public class a_twoSum {
    public static void main(String[] args) {
        int[] ns = {2, 7, 9, 11, 15};
        int t = 9;
        twosum ab = new twosum();
        int[] s = ab.twoSum(ns, t);
        System.out.println(Arrays.toString(s));
    }
}

//System.out.println();


class twosum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashtable = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; ++i) {
            if (hashtable.containsKey(target - nums[i])) {
                return new int[]{hashtable.get(target - nums[i]), i};
            }
            hashtable.put(nums[i], i);
        }
        return new int[0];
    }
}


