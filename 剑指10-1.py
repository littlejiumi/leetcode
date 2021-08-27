class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            tmp = b
            b = (a + b)%1000000007
            a = tmp
        return a
