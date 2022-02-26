# 对于乘法，我们需要注意，负数乘以负数，会变成正数，所以解这题的时候我们需要维护两个变量，当前的最大值，以及最小值，最小值可能为负数，
#但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxN = minN = res = nums[0]
        for i in range(1, len(nums)):
            temp1 = maxN * nums[i]
            temp2 = minN * nums[i]
            maxN =  max(nums[i], max(temp1, temp2))
            minN = min(nums[i], min(temp1, temp2))
            res = max(res, maxN)
        return res
