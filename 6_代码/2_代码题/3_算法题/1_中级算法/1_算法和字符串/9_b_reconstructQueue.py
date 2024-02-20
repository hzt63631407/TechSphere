

# leetcode 406. 根据身高重建队列

# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
#
# 每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
#
# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，
#
# 其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。

# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]


# 一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，
#
# 或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。
#
# 在本题目中，我首先对数对进行排序，按照数对的元素 1 降序排序，
#
# 按照数对的元素 2 升序排序。原因是，按照元素 1 进行降序排序，对于每个元素，
#
# 在其之前的元素的个数，就是大于等于他的元素的数量，
#
# 而按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res


