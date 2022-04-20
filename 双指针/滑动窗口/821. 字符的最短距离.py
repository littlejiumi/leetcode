class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a, b = [float("inf") for _ in range(len(s))], [float("inf") for _ in range(len(s))]
        flag = 0
        for i in range(len(s)):
            if s[i] == c:
                a[i] = 0
                flag = 1
            elif flag != 0:
                a[i] = flag
                flag += 1
        flag = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                b[i] = 0
                flag = 1
            elif flag != 0:
                b[i] = flag
                flag += 1
        res= []
        for i in range(len(s)):
            res.append(min(a[i], b[i]))
        return res
