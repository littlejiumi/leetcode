class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        i = 0
        while i <= cover:
            cover = max(cover, nums[i]+i)
             # 看覆盖范围是否能覆盖最后一个下标
            if cover >= len(nums)-1: return True
            i+=1
        return False
