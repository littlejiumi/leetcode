class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path= [], []
        def backtrack(nums, startIndex):
            res.append(path[:])
            if(startIndex == len(nums)): return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return res
