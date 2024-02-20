

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）

def letterCombinations(self, digits: str) -> List[str]:
    d = {'2' :'abc' , '3' :'def' , '4' :'ghi' , '5' :'jkl' , '6' :'mno',
         '7' :'pqrs', '8' :'tuv', '9' :'wxyz'}
    if not digits:
        return []
    res = ['']
    for i in digits:
        length = len(res)
        for n in range(length):
            temp = res.pop(0)
            for j in d[i]:
                res.append(''.join([temp, j]))
    return res