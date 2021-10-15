class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            # 最终利润是可以分解的,只要比昨天涨了就算
            if prices[i] > prices[i-1]:
                res += prices[i]-prices[i-1] 
        return res
            
