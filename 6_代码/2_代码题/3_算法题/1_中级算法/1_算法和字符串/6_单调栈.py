

# 单调栈 是一种特殊的堆栈的形式。它在栈的「先进后出」规则基础上，
# 要求「从栈顶到栈底的元素是单调递增（或者单调递减）」。

# 例子1
# l = [3,4,5,1,3,4,6]
# s = []
# for i in range(len(l)):
# 	if s == []:
# 		s.append(l[i])
# 	else:
# 		if s[-1] < l[i]:
# 			s.append(l[i])
# print(s)

l = [3,4,5,1,3,4,3,6]
s = []
for i in range(len(l)):
	if s == []:
		s.append(l[i])
	else:
		while s and s[-1] >= l[i]:
			s.pop()
		s.append(l[i])
print(s)