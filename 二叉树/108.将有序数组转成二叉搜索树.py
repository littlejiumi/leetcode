# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traveral(nums, L, R):
            if L > R: return None
            mid = (L + R) // 2
            root = TreeNode(nums[mid])
            root.left = traveral(nums, L, mid-1)
            root.right = traveral(nums, mid+1, R)
            return root
        return traveral(nums, 0, len(nums)-1)
