
# 描述
# 现在有2副扑克牌，从扑克牌中随机五张扑克牌，我们需要来判断一下是不是顺子。
# 有如下规则：
# 1. A为1，J为11，Q为12，K为13，A不能视为14
# 2. 大、小王为 0，0可以看作任意牌
# 3. 如果给出的五张牌能组成顺子（即这五张牌是连续的）就输出true，否则就输出false。
# 4.数据保证每组5个数字，每组最多含有4个零，数组的数取值为 [0, 13]

class Solution:
    def IsContinuous(self, numbers: List[int]) -> bool:
        # write code here
        mi, ma = 14, 0
        a = []
        for i in numbers:
            if i == 0:
                continue
            if i not in a:
                a.append(i)
            else:
                return False
            if i < mi:
                mi = i
            if i > ma:
                ma = i
        if ma - mi < 5:
            return True
        else:
            return False

# class Solution:
#     def IsContinuous(self , numbers: List[int]) -> bool:
#         # write code here
#         repeat = []
#         ma, mi = 0, 14
#         for num in numbers:
#             if num == 0:
#                 continue  # 跳过大小王
#             ma = max(ma, num)  # 最大牌
#             mi = min(mi, num)  # 最小牌
#             if num in repeat:
#                 return False  # 若有重复，提前返回 false
#             repeat.append(num)  # 添加牌至 Set
#         return ma - mi < 5