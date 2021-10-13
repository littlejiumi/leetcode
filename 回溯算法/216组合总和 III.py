class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, path = [], []
        def dfs(k, n, startIndex, sum):
            if n == sum and k == 0:
                res.append(path[:])
                return
            for i in range(startIndex, 10):
                path.append(i)
                sum += i
                dfs(k-1, n, i+1, sum)
                path.pop()
                sum -= i
        dfs(k, n, 1, 0)
        return res
