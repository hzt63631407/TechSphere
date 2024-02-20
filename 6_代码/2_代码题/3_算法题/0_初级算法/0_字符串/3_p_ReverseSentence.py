
# 输入：
# "nowcoder. a am I"
# 复制
# 返回值：
# "I am a nowcoder."

def ReverseSentence(str: str) -> str:
    # write code here
    strs = str.split()  # 分割字符串,变成列表
    print(strs)
    strs.reverse()  # 翻转单词列表
    return ' '.join(strs)  # 拼接为字符串并返回

ReverseSentence("nowcoder. a am I")

