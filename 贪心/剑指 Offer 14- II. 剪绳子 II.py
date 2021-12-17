class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n-1
        res = 1
        while n > 4:
            res = res * 3 %(1e9+7)
            n -= 3
        return int((res * n )%(1e9+7))
            
