# 999 = 9 * 1 + 9 * 10 + 9 * 100
# 999 = 10^3 - 1
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        cnt = 9
        tmp = 1
        while n>1:
            tmp *= 10
            cnt += tmp * 9
            n -=1
        return [i for i in range(1, cnt+1)]
      
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        maxNum = pow(10, n)
        result = []
        for i in range(1, maxNum):
            result.append(i)
        return result
