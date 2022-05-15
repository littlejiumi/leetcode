class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res= []
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        res.append(l)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        res.append(r)
        if res[0]>res[1]:return [-1,-1]
        return res
        
