/*
记dp[i][j]表示字符串word1[:i]和word2[:j]的最小编辑距离，
那么如果word1[i]与word2[j]相同，新的最小编辑距离dp[i+1][j+1]为之前的最小编辑距离dp[i][j]；
否则，最新的最小编辑距离为从word1里删除word1[i]或者从word2[j]里删除j或者将word1[i]或word2[j]替换为相等得到，也就是min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1

初始化，一个字符为空，另一个字符不为空，编辑代价为字符串长度
*/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(m):
            dp[i + 1][0] = i + 1
        for j in range(n):
            dp[0][j + 1] = j + 1
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[m][n]
