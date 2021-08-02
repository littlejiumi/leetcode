class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = {}
        for num in nums:
            hashset[num] = hashset[num] + 1 if hashset.get(num) else 1
        for key, value in hashset.items():
            if value > len(nums) / 2:
                return key
        return 0
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
