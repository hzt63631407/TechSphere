

import random

# random.random(): 返回随机生成的一个浮点数，范围在[0,1)之间
print(random.random())


# random.randint(a,b)：生成指定范围内的整数
print(random.randint(1,10))


# random.choice()：从指定的序列中获取一个随机元素
print(random.choice(['good', 'hello', 'is', 'hi', 'boy']))   # 从list列表中随机取
print(random.choice(('str', 'tuple', 'list')))   # 从tuple元组中随机取


# random.shuffle(x[,random])：用于将一个列表中的元素打乱，随机排序
p=['hehe','xixi','heihei','haha','zhizhi','lala','momo..da']
random.shuffle(p)
print(p)
x = [1, 2, 3, 4, 5]
random.shuffle(x)
print(x)


# random.sample(sequence,k)：用于从指定序列中随机获取指定长度的片段，sample()函数不会修改原有序列。
list1 = [1,2,3,4,5,6,7,8,9,10]
s = "123"
slice1 = random.sample(list1,3)
slice2 = random.sample(s,1)
print(slice2)

# #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = random.sample(range(0, 10), 5)
# print(x, type(x))
# #[9, 2, 7, 8, 6] <class 'list'>
# Words = "AppleKMedoide"
# print(random.sample(Words, 3))
# #['p', 'M', 'A']
# print(random.sample(Words, 3))
# #['d', 'i', 'l']