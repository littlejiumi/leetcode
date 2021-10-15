class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path, used = [], [], []
        def backtrack(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i in used: continue
                path.append(nums[i])
                used.append(i)
                backtrack(nums, used)
                used.pop()
                path.pop()
        backtrack(nums, used)
        return res
