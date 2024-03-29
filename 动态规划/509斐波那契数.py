class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:                     # 注意先确定初始情况
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]






class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            a, b= 0, 1
            c = 0
            for i in range(2, n+1):
                c = a + b
                a = b
                b = c
            return b
