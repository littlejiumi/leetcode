class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1) # dp[i]表示长度为i的绳子剪成m端后长度的最大乘积(m>1)
        dp[2] = 1 # 递归边界
        for i in range(3, n + 1): # 对于3+的绳子
            for j in range(2, i):  # 首先对绳子剪长度为j的一段,其中取值范围为 2 <= j < i
     # 取所有dp[i]最大的，所以第一项；剩下了i-j长度，取直接乘或者dp的值中较大的那个
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]
