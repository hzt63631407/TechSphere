# 有一个数组，是所有的员工的年龄
# 如：[22,23,26,22,34,25,26,27,23,30,29]
# 假设数组的长度很大，进行排序


age = [22,23,26,22,34,25,26,27,23,30,29]

def age_sort(nums):
    d = {}
    b = []
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    a = sorted(d.items(),key=lambda x:x[0])
    print(a)
    for i in range(len(a)):
        b += [a[i][0]] * int(a[i][1])
    return b

print((age_sort(age)))


