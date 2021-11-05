class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n): # 一个字符肯定回文了，是动态规划的边界条件
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度L
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break                   
                if s[i] != s[j]:  # 如果首尾不等
                    dp[i][j] = False 
                else:             # 如果首尾相等
                    if j - i <= 2: # 2（,3）个字符：如果首尾相等则是回文
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
