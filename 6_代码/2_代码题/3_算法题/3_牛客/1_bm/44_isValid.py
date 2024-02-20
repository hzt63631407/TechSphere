
# 描述
# 给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
# 括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        dic = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        l = []
        for i in s:
            if i in dic:
                if l != [] and dic[i] == l[-1]:
                    l.pop()
                else:
                    l.append(i)
            else:
                l.append(i)
        if l == []:
            return True
        else:
            return False