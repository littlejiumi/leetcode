class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path, used = [], [], []
        def backtrack(nums, used):
            if len(nums) == len(path):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i-1]==nums[i] and (i-1 not in used):
                    continue  # 只比全排列多了这一行
                if i in used: continue
                path.append(nums[i])
                used.append(i)   # 注意，不能放nums[i]，因为有重复的元素。存放index是唯一的。
                backtrack(nums, used)
                used.pop()
                path.pop()
        nums.sort()
        backtrack(nums, used)
        return res
