# 哈希表 时间O(n)，空间O（n）
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        repeatDict = {}  # dict
        for num in nums:
            if num not in repeatDict:
                repeatDict[num] = 1
            else:
                return num
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            if num in numset:
                return num
            else:
                numset.add(num)
# 先排序，然后看相邻元素是否有相同的，有直接return。 不过很慢，时间O(nlogn)了，空间O(1)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for idx in range(1, n):
            if nums[idx-1] == nums[idx]:
                return nums[idx]
# 时间复杂度O(n)，空间复杂度O(1)。可以看做是一种原地哈希，不过没有用到字典。具体做法就是因为题目中给的元素是 < len（nums）的，
# 所以我们可以让 位置i 的地方放元素i。如果位置i的元素不是i的话，那么我们就把i元素的位置放到它应该在的位置，即 nums[i] 和nums[nums[i]]的元素交换，
# 这样就把原来在nums[i]的元素正确归位了。如果发现 要把 nums[i]正确归位的时候，发现nums[i]（这个nums[i]是下标）那个位置上的元素和要归位的元素已经一样了，说明就重复了，重复了就return
class Solution:
    def findRepeatNumber(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:              
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
