class Solution:
    def translateNum(self, num: int) -> int:
        s= str(num)
        size = len(s)
        a = b = 1
        for i in range(1, size):
            c = a + b if "10"<=s[i-1:i+1]<="25" else b
            a = b
            b = c
        return b

