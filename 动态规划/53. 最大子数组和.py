class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(0, nums[i-1])
            if nums[i] > res: res = nums[i]
        return res
