
# leetcode 735. 行星碰撞
#
# 给定一个整数数组 asteroids，表示在同一行的行星。
#
# 对于数组中的每一个元素，其绝对值表示行星的大小，
# 正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
#
# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
# 如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
#
# 输入：asteroids = [5,10,-5]
# 输出：[5,10]
# 解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
#
# 答案
# 假设栈中顶部元素为 top，一个新的小行星 new 进来了。如果 new 向右移动（new>0），
# 或者 top 向左移动（top<0），则不会发生碰撞。
# 否则，如果 abs(new) < abs(top)，则新小行星 new 将爆炸；
# 如果 abs(new) == abs(top)，则两个小行星都将爆炸；
# 如果 abs(new) > abs(top)，
# 则 top 小行星将爆炸（可能还会有更多小行星爆炸，因此我们应继续检查）。

def asteroidCollision(self, asteroids):
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return ans

