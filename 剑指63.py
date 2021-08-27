class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost, maxProfit = 1000000, 0
        for p in prices:
            minCost = min(p, minCost) # 之前最低价
            maxProfit = max(maxProfit, p - minCost) # 动态规划，取前一个最大利润和（现价-之前最低价）较大值
        return maxProfit
