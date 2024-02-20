package i_算法题.a_初级算法题.b_数组;


// leetcode 724
//给你一个整数数组 nums ，请计算数组的 中心下标 。
//数组 中心下标 是数组的一个下标，
//其左侧所有元素相加的和等于右侧所有元素相加的和。


public class d_moveZeroes {
    public void moveZeroes(int[] nums) {
        int s=0;//定义收集不是0的数的指针
        //开始收集不是零的数
        for (int i = 0; i < nums.length ;i++) {
            if(nums[i]!=0){
                nums[s++] = nums[i];
            }
        }
        //收集完毕后,后面自然就都是0了
        for (int i = s; i < nums.length; i++) {
            nums[i]=0;
        }
    }

}
