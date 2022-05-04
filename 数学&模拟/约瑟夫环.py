class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1 : return 1
        ans =  (k + self.findTheWinner(n - 1, k) - 1) % n + 1
        return ans
