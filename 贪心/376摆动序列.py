class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        if nums[0] == nums[1]: 
            res = 1  # 记录峰值个数
            pre = 0  # 记录第一个差值是多少
        else: 
            res = 2
            pre = nums[1] - nums[0]
        for i in range(2, len(nums)):
            cur = nums[i] - nums[i-1]
            if cur and cur * pre <= 0:  # 当前差值不为0 且 与前一差值不同号，才能+1
                res += 1
                pre = cur
        return res
        
