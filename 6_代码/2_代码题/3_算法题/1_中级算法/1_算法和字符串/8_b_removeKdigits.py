
# leetcode 402. 移掉 K 位数字

# 给你一个以字符串表示的非负整数 num 和一个整数 k ，
# 移除这个数中的 k 位数字，使得剩下的数字最小。
# 请你以字符串形式返回这个最小的数字。
#
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。

# 思路，从左到右，找第一个比后面大的字符，删除，清零，k次扫描。

# 单调递增栈：单调递增栈就是从栈底到栈顶数据是从大到小
# 单调递减栈：单调递减栈就是从栈底到栈顶数据是从小到大

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k > 0:
            stack = stack[:-k]                  # 这是python的切片机制，表示从头到倒数第k个 剩下123578 k还有3 即123
        if ''.join(stack).lstrip('0') == "":    # lstrip() 方法用于截掉字符串左边的空格或指定字符，左边的0被截掉
            return "0"
        return ''.join(stack).lstrip('0')
        # return ''.join(stack).lstrip('0') or "0"

# lstrip() 方法用于截掉字符串左边的空格或指定字符。

str = "     this is string example....wow!!!     "
print( str.lstrip() )
str = "88888888this is string example....wow!!!8888888"
print( str.lstrip('8') )

print([1]or'0')
print(''or'0')