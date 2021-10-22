# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 终止条件：空节点/p或q等于root
        if not root or root == p or root == q: return root
        # 遍历左子树，右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 中：如果没找到，返回另一枝
        if not left: return right
        if not right: return left
        # 都找到了，说明就是root
        return root
