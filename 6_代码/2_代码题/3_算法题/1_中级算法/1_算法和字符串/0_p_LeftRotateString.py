
# 描述
# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
# 对于一个给定的字符序列  S ，请你把其循环左移 K 位后的序列输出。例如，字符序列 S = ”abcXYZdef” ,
# 要求输出循环左移 3 位后的结果，即 “XYZdefabc”


# 输入：
# "abcXYZdef",3
# 返回值：
# "XYZdefabc"

# 输入:
# "aab",10
#
# 返回值:
# "aba"

def LeftRotateString(self , s: str, n: int) -> str:
    # write code here
    s1 = ""
    s2 = ""
    if len(s) == 0:
        return ""
    n = n % len(s)
    for i in range(0 ,n):
        s1 = s1 + str(s[i])
    for i in range(n ,len(s)):
        s2 = s2 + str(s[i])
    return s2 + s1