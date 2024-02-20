
# 用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)
# 和n次在队列头部删除整数(pop)的功能。
# 队列中的元素为int类型。保证操作合法，即保证pop操作时队列内已有元素。

# 答案
# 借助栈的先进后出规则模拟实现队列的先进先出
# 1、当插入时，直接插入 stack1
# 2、当弹出时，当 stack2 不为空，弹出 stack2 栈顶元素，如果 stack2 为空，
# 将 stack1 中的全部数逐个出栈入栈 stack2，再弹出 stack2 栈顶元素

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# 描述
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，
# 输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。
#
# 此栈包含的方法有：
# push(value):将value压入栈中
# pop():弹出栈顶元素
# top():获取栈顶元素
# min():获取栈中最小元素

# class Solution:
#     def __init__(self):
#         self.stack = []
#     def push(self, node):
#         # write code here
#         self.stack.append(node)
#     def pop(self):
#         if self.stack != None:
#             self.stack.pop()
#         # write code here
#     def top(self):
#         if self.stack != None:
#             return self.stack[-1]
#         else:
#             return None
#         # write code here
#     def min(self):
#         if self.stack != None:
#             return min(self.stack)
#         else:
#             return None
