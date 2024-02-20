




# 判断两颗二叉树是否相等


def isSameTree(p, q):
    if p == None and q == None:
        return True
    # 自身比，左右各自再比
    elif p and q :
        return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False

