class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        tmp = 0
        for i in nums:
            tmp += i
            m = max(tmp, m)
            if tmp<0: tmp = 0  # 若当前和小于0，则舍去，从0开始加
        return m
