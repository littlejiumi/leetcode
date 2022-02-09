class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]: return 0
        minP = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] <= minP: minP = prices[i]
            else: res = max(prices[i]-minP, res)
        return res
