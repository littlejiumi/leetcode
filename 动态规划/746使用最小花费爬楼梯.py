class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # 注意最后一步可以理解为不用花费，所以取倒数第一步，第二步的最小值
        return min(dp[n-1], dp[n-2])
