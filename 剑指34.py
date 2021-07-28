# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        result, path = [], []
        def recur(root, target):
            if not root: return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                result.append(list(path)) #相当于复制了一个 path 并加入到 result
            recur(root.left, target)
            recur(root.right, target)
            path.pop()
        recur(root, target)
        return result
