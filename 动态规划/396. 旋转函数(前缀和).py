class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        Sum = sum(nums)
        dp = [0] * len(nums)
        dp[0] = sum([idx * num for idx, num in enumerate(nums)])
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + Sum - nums[-i]*len(nums)
        return max(dp)
        

