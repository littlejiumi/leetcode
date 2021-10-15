class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, cur):
            # 先判断不成立的
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or not board[i][j] == word[cur]:
                return False
            # 成立的
            if cur == len(word)-1:return True
            temp = board[i][j]  # 保存目前遍历的字母
            board[i][j] = ''    # 去除
            result = dfs(i+1, j, cur+1) or dfs(i, j + 1, cur+1) or dfs(i-1,j,cur+1) or dfs(i, j-1,cur+1)
            board[i][j] = temp  # 恢复
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
