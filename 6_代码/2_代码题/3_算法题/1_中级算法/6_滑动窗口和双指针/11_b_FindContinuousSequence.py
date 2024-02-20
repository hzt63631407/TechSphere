

# JZ74 和为S的连续正数序列
#
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,
# 他马上就写出了正确答案是100。但是他并不满足于此,
# 他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
# 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?

def FindContinuousSequence(self , sum: int) -> List[List[int]]:
    res = []
    # 从1到2的区间开始
    l = 1
    r = 2
    while l < r:
        # 计算区间内的连续和
        sum1 = (l + r) * (r - l + 1) / 2
        # 如果区间内和等于目标数
        if sum1 == sum:
            temp = []
            # 记录区间序列
            for i in range(l, r + 1):
                temp.append(i)
            res.append(temp)
            # 左区间向右
            l += 1
        # 如果区间内的序列和小于目标数，右区间扩展
        elif sum1 < sum:
            r += 1
        # 如果区间内的序列和大于目标数，左区间收缩
        else:
            l += 1
    return res