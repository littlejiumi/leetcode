class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set1=set(nums)
        sums=sum(set1)*2
        return(sums-sum(nums))
