class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j):
            if not 0<=i<=m-1 or not 0<=j<=n-1 or (i,j) in visited or i%10+i//10+j%10+j//10>k:return 0
            visited.add((i,j))    # vis之后记住，不用回溯
            result = 1+dfs(i+1,j)+dfs(i,j+1)   # 记住这个计数的方式！跟二叉树题一样
            return result
        visited = set()
        return dfs(0,0)
