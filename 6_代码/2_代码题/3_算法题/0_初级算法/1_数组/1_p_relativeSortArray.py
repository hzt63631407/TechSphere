
# leetcode1122. 数组的相对排序
#
# 给你两个数组，arr1 和 arr2，arr2 中的元素各不相同，
# arr2 中的每个元素都出现在 arr1 中。
#
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
# 未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。


def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    a = set(arr1) - set(arr2)
    arr2 = arr2 + sorted(a)
    arr1.sort(key=arr2.index)
    return arr1

# sort(key=arr2.index) 就是按arr2元素对应的下标顺序进行排序,