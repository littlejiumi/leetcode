class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        flag =  -1
        row = 0
        for i in s:
            res[row] += i
            if row == 0 or row == numRows-1: flag = -flag
            row += flag
        return "".join(res)
