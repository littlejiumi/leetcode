# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def constructTree(nums, L, R):
            if L > R: return None
            maxNum = L
            for i in range(L+1, R+1):
                if nums[i] > nums[maxNum]:
                    maxNum = i
                    
            root = TreeNode(nums[maxNum])
            root.left = constructTree(nums, L, maxNum-1)
            root.right = constructTree(nums, maxNum+1, R)
            return root

        return constructTree(nums, 0, len(nums)-1)
