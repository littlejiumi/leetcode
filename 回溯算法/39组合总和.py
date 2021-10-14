class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, target, sum, startIndex):
            if sum > target: return
            if sum == target:
                res.append(path[:])  # 重要，别忘啦
                return 
            for i in range(startIndex, len(candidates)):
                if sum + candidates[i] >  target: return # 剪枝：如果 sum + candidates[i] > target 就终止遍历
                sum += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, target, sum, i)  # startIndex = i:表示可以重复读取当前的数
                sum -= candidates[i]
                path.pop()
                
        res, path = [], []
        candidates.sort()  # 排序
        backtracking(candidates, target, 0, 0)
        return res
