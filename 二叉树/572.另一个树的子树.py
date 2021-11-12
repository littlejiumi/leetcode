# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def compare(root1, root2):
            if not root1 and not root2: return True
            elif not root1 or not root2: return False
            elif not root1.val == root2.val: return False
            return compare(root1.left, root2.left) and compare(root1.right, root2.right)
        if not root: return False
        elif compare(root, subRoot): return True
        L = self.isSubtree(root.left, subRoot)
        R = self.isSubtree(root.right, subRoot)
        return L or R
    
