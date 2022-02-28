# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, prel, prer, inorder, inl, inr):
            if prel > prer: return
            root = TreeNode(preorder[prel])
            inroot = inl
            while inorder[inroot] != preorder[prel]: inroot+=1
            leftlen = inroot - inl
            root.left = build(preorder, prel+1, prel+leftlen, inorder, inl, inroot-1)
            root.right = build(preorder, prel+leftlen+1, prer, inorder, inroot+1, inr)
            return root
        return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
