class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            while nums[l] % 2 == 0 and l < n-1:
                l += 1
            while nums[r] % 2 != 0 and r > 0:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        return nums
