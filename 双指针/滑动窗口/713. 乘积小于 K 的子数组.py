class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0 or k== 1: return 0
        product = 1
        res, left = 0, 0
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            res += right - left + 1 # 包含右边界值的子串个数刚好是r-l+1
        return res
