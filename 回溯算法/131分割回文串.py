class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        def backtracking(s, startIndex):
            if startIndex == len(s):
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                p = s[startIndex: i+1]
                if p == p[::-1]: path.append(p)
                else: continue
                backtracking(s, i+1)
                path.pop()
        backtracking(s, 0)
        return res
