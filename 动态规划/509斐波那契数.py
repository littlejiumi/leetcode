class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            a, b= 0, 1
            c = 0
            for i in range(2, n+1):
                c = a + b
                a = b
                b = c
            return c
