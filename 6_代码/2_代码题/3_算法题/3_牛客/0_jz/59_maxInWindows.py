

# 描述
# 给定一个长度为 n 的数组 nums 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。
# 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
# 他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
# {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
# {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。


def maxInWindows(self , num: List[int], size: int) -> List[int]:
    # write code here
    if size == 0:
        return []
    ans = []
    l = 0
    for i in range(len(num) - size + 1):
        a = num[i:i + size]
        temp = max(a)
        ans.append(temp)
    return ans


def maxInWindows(self, num, size):
    # write code here
    # 双端队列
    queue = []
    # 返回列表
    res = []
    i = 0
    while size>0 and i<len(num):
        if len(queue)>0 and i-size+1>queue[0]: #超出范围的去掉
            queue.pop(0)
    # 当前值大于之前的值，之前的不可能是最大值，可以删掉
        while len(queue)>0 and num[queue[-1]]< num[i]:
            queue.pop()
    # 进入队列
        queue.append(i)
        if i>= size-1: #此时开始是第一个滑动窗口
            res.append(num[queue[0]])
        i+=1
    return res