

# 1.count()函数：
# 统计在字符串/列表/元组中某个字符出现的次数，参数可以设置起始位置或结束位置。

# str = "i love python,i am learning python"
# print(str.count("i")) #star 和end 为默认参数

# list = ['1','2','1']
# print(list.count('1'))        # 输出2

# 2.counter()函数：
from collections import Counter
lists = ['a', 'a', 'b', 5, 6, 7, 5]                             # 可以是list，也可以是string
a = Counter(lists)
print(a)  # Counter({'a': 2, 5: 2, 'b': 1, 6: 1, 7: 1})          # counter类型 不是dict
# 求子串的时候会用到


# 3.计算可以用到dict
# lists = ['a','a','b',5,6,7,5]
#   count_dict = dict()
#   for item in lists:
#    if item in count_dict:
#     count_dict[item] += 1
#    else:
#     count_dict[item] = 1