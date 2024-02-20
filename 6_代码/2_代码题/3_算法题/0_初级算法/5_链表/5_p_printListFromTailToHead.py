

# 输入一个链表的头节点，按链表从尾到头的顺序返回每个节点的值
# （用数组返回）。

# 输入：{1,2,3}
# 返回值：[3,2,1]



def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
    # write code here
    ans = []
    while listNode:
        ans.append(listNode.val)
        listNode = listNode.next
    ans.reverse()
    return ans