# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val!=B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)
        if not A or not B:return False # 边界条件判断，如果A和B有一个为空，返回false
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) #先从根节点判断B是不是A的子结构，如果不是在分别从左右两个子树判断，只要有一个为true，就说明B是A的子结构
