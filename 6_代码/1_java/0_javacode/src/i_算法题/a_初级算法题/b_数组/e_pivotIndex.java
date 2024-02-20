package i_算法题.a_初级算法题.b_数组;

//leetcode 219
//给你一个整数数组 nums 和一个整数 k ，
//判断数组中是否存在两个 不同的索引 i 和 j ，
//满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
//如果存在，返回 true ；否则，返回 false 。


public class e_pivotIndex {
    public int pivotIndex(int[] nums) {
        int right = 0;
        int left = 0;
        for(int num : nums) right += num;
        for(int i = 0; i < nums.length; i++) {
            right -= nums[i];
            if(right == left) return i;
            left += nums[i];
        }
        return -1;
    }
}
