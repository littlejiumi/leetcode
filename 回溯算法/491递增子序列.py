class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        def backtrack(nums, startIndex):
            repeat = set()   # 树层不能重复
            if len(path) > 1: res.append(path[:])    # 不需要终止条件，只需大于等于2就放进res
            for i in range(startIndex, len(nums)):
                if nums[i] in repeat: continue
                if len(path) >= 1 and path[-1] > nums[i]:   # 如果不是递增的
                    continue
                repeat.add(nums[i])
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return res
