class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minP = prices[0]
        for i in prices:
            if i < minP:
                minP = i
            if i > minP:
                res = max(res, i-minP)
        return res
