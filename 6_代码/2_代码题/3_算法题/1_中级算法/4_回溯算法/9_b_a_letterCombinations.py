# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。




# 答案    # 电话号码 放弃
def letterCombinations(self, digits: str) -> list[str]:
    dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    size = len(digits)
    ans = []
    if size == 0:
        return ans
    chars = []
    for i in digits:
        chars.append(dic.get(i))
    res = []
    def backtrack(res, index):
        if len(res) == size:
            ans.append(''.join(res))
            return
        for i in range(index, size):
            for j in range(len(chars[i])):
                res.append(chars[i][j])
                backtrack(res, i + 1)
                res.pop()
    backtrack(res, 0)
    return ans
