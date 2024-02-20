

# 描述
# 有一个整数数组，请你根据快速排序的思路，找出数组中第 k 大的数。
# 给定一个整数数组 a ,同时给定它的大小n和要找的 k ，
# 请返回第 k 大的数(包括重复的元素，不用去重)，保证答案存在


class Solution:
    def findKth(self , a: List[int], n: int, K: int) -> int:
        # write code here
        def QuickSort(num):
            if len(num) <= 1: #边界条件
                return num
            key = num[0] #取数组的第一个数为基准数
            llist,rlist,mlist = [],[],[key]     #定义空列表，分别存储小于/大于/等于基准数的元素
            for i in range(1,len(num)):         #遍历数组，把元素归类到3个列表中
                if num[i] > key:
                    rlist.append(num[i])
                elif num[i] < key:
                    llist.append(num[i])
                else:
                    mlist.append(num[i])
            return QuickSort(llist)+mlist+QuickSort(rlist)
        l = QuickSort(a)
        l.reverse()
        print(l)
        return l[K-1]