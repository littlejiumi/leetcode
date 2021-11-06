class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path, res = [], []
        used = [0] * len(nums)
        def backtracking(nums, startIndex, used):
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                if i > startIndex and used[i]==0 and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                used[i]=1
                backtracking(nums, i+1, used)
                used[i] = 0
                path.pop()
        nums.sort()
        backtracking(nums, 0, used)
        return res
