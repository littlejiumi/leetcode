class Solution:
    def permutation(self, s: str) -> List[str]:
        used = [0] *  len(s)
        res, path = [], []
        def dfs(s, used):
            if len(path) == len(s):
                res.append("".join(path))
            for i in range(len(s)):
                if i > 0 and s[i-1] == s[i] and used[i-1]==0: continue
                if used[i] == 0:
                    used[i] = 1
                    path.append(s[i])
                    dfs(s, used)
                    path.pop()
                    used[i] = 0
        li = sorted(list(s))
        s = "".join(li)
        dfs(s, used)
        return res
