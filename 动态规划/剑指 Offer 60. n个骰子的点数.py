class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1 / 6] * 6
        for i in range(2, n + 1):  # n个骰子
            tmp = [0] * (5 * i + 1) # 此时5n+1种情况
            for j in range(len(dp)): # 上一层n-1个骰子时的结果上，加上1～6点数均概率的情况
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp
