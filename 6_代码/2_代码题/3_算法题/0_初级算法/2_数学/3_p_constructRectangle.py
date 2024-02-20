#
# 492. 构造矩形
# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。
# 所以，现给定一个具体的矩形页面面积，
# 你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
#
# 你设计的矩形页面必须等于给定的目标面积。
# 宽度 W 不应大于长度 L ，换言之，要求 L >= W 。
# 长度 L 和宽度 W 之间的差距应当尽可能小。
# 返回一个 数组 [L, W]，其中 L 和 W 是你按照顺序设计的网页的长度和宽度。
#
#
# 示例1：
#
# 输入: 4
# 输出: [2, 2]
# 解释: 目标面积是 4， 所有可能的构造方案有 [1 ,4], [2 ,2], [4 ,1]。
# 但是根据要求2，[1 ,4] 不符合要求;
# 根据要求3，[2 ,2] 比 [4 ,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。


# 答案
# 我们可以初始化W =sqrt(area) ,能否被 W 整除，如果可以则跳出循环，否则将 WW 减一后继续循环。

def constructRectangle(self, area: int) -> List[int]:
    w = int(sqrt(area))
    while area % w:
        w -= 1
    return [area // w, w]

