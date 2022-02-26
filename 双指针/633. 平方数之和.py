class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            temp = l**2 + r**2
            if temp == c:return True
            elif temp < c: l += 1
            else: r -= 1
        return False
