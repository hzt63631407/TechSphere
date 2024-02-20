package i_算法题.a_初级算法题.b_数组;

import java.util.HashMap;
import java.util.Map;

//leetcode 283
//给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
//同时保持非零元素的相对顺序。

public class d_containsNearbyDuplicate {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; ++i){
            if(map.containsKey(nums[i])){
                if((i - map.get(nums[i]) <= k)) return true;
            }
            // 覆盖之后的位置和下一个相同值肯定离得更近
            map.put(nums[i], i);
        }
        return false;
    }
}
