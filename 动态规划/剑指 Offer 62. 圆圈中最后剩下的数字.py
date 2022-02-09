class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0 # dp[1]=0
        for i in range(2, n + 1):
            x = (x + m) % i #dp[i]=(dp[i−1]+m)%i
        return x
