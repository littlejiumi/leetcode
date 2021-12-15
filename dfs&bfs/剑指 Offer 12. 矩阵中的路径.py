class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[0] * n for _ in range(m)]
        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k] or vis[i][j] == 1: return False
            if k == len(word)-1: return True
            vis[i][j] = 1
            res = dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
            vis[i][j] = 0
            return res
        for i in range(m):
            for j in range(n):
                res = dfs(i, j, 0)
                if res: return True
        return False

