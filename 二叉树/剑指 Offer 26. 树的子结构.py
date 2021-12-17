# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True   #子结构 B遍历完了就行
            if not A or A.val!=B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)
        if not A or not B:return False
        # 简写的前序遍历
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
