class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = Sum = nums[0]
        # Sum为i-1结尾的最大连续子数组。i时Sum+=nums[i]，
        # 但如果Sum<0就当作0，最大连续子数组就是nums[i]本身
        for i in range(1, len(nums)):
            if Sum < 0: Sum = 0
            Sum += nums[i]
            res = max(res, Sum)
        return res




