class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1 : return 1
        ans =  (k + self.findTheWinner(n - 1, k) - 1) % n + 1
        return ans
# 约瑟夫环问题的递推公式： f(n)= (f(n - 1) + k - s) % n + 1 `s`开始起点数, `k`间隔数, `n`玩家个数
# 通解： return s if n == 1 else (self.findTheWinner(n-1, k) + k - s) % n + s

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (self.findTheWinner(n-1, k) + k - 1) % n + 1
