
# leetcode 495. 提莫攻击
#
# 在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄。
#
# 他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。
#
# 当提莫攻击艾希，艾希的中毒状态正好持续 duration 秒。
#
# 正式地讲，提莫在 t 发起发起攻击意味着艾希在时间区间 [t, t + duration - 1]
#
# （含 t 和 t + duration - 1）处于中毒状态。
#
# 如果提莫在中毒影响结束 前 再次攻击，中毒状态计时器将会 重置 ，
#
# 在新的攻击之后，中毒影响将会在 duration 秒后结束。

def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    ans = 0
    for i in range(len(timeSeries) - 1):
        if timeSeries[i] + duration <= timeSeries[i + 1]:
            ans += duration
        else:
            ans += timeSeries[i + 1] - timeSeries[i]
    return ans + duration