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
