package i_算法题.a_初级算法题.b_数组;


//leetcode 485
//给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

public class f_findMaxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0, count = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                count++;
            } else {
                maxCount = Math.max(maxCount, count);
                count = 0;
            }
        }
        maxCount = Math.max(maxCount, count);
        return maxCount;
    }
}

// todo 需要精简，参考python的解法

