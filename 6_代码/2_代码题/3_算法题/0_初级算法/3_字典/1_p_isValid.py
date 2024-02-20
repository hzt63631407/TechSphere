# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

# 自己    # 答案
def isValid(self, s: str) -> bool:
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


# 答案
def isValid(s):
        if len(s) % 2 == 1:
            return False
        dic = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for i in s:
            if stack and i in dic:              # 如果stack存在而且i是右阔号
                if stack[-1] == dic[i]:         # 最后一个元素和右括号匹配
                    stack.pop()                 # 移除最后一个元素
                else:
                    return False
            else:
                stack.append(i)
        return not stack


# dic = {"a":1,"b":2,"c":3}
# for i in dic:
#     print(i)
#     print(dic[i])

if __name__ == "__main__":
    s1 = "([)]"
    s2 = "{[]}"
    s3 = "()[]{})("                          # 如果是这种 自己的会出现问题
    # print(is_valid(s3))
    print(isValid(s1))