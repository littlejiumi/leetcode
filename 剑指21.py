class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        return odd + even
        
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 1:
                left += 1
            while left <= right and nums[right] % 2 == 0:
                right -= 1
            if left > right:  # 重要！
                break
            nums[left], nums[right] = nums[right], nums[left]
        return nums
     
 class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1
            fast += 1
        return nums

