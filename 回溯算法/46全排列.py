class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        used = [0] * len(nums)
        def backtracking(nums, used):  # 全排列问题不需要startIndex，但是需要used数组
            if len(nums) == len(path):
                res.append(path[:])
            for i in range(len(nums)):
                if used[i] == 1: continue
                used[i] = 1
                path.append(nums[i])
                backtracking(nums, used)
                path.pop()
                used[i] = 0
        backtracking(nums, used)
        return res
