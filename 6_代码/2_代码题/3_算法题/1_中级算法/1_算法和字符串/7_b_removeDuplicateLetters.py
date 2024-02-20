
# 316. 去除重复字母
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
# 需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
#
# 示例 1：
#
# 输入：s = "bcabc"
# 输出："abc"

# 如果队列是有顺序的，可以用单调栈
# 单调递增栈：单调递增栈就是从栈底到栈顶数据是从大到小
# 单调递减栈：单调递减栈就是从栈底到栈顶数据是从小到大


# 自己
def removeDuplicateLetters(self, s: str) -> str:
    a = []
    for i in range(len(s)):
        if a == []:
            a.append(s[i])
        if s[i] in a:
            continue
        while a and s[i] < a[-1] and a[-1] in s[i + 1:]:
            a.pop()
        a.append(s[i])
    return "".join(a)


def removeDuplicateLetters(self, s: str) -> str:
    # 使用单调栈 思路就是 遇到一个新字符 
    # 如果比栈顶小 并且在新字符后面还有和栈顶一样的 就把栈顶的字符抛弃了 注意需要多次进行判断
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] in stack:
            continue
        else:
            while stack and stack[-1] > s[i] and stack[-1] in s[i + 1:]:  # 用while
                stack.pop()
            stack.append(s[i])

    return "".join(stack)
