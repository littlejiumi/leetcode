class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
                continue
            if i > 0 and nums[i]==nums[i-1]:
                return False
        return nums[4]-nums[count]<=4
            
