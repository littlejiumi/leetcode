class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        res, num = 100, 0
        had = set()
        def dfs(start, end, bank, num):
            if start == end: 
                nonlocal res
                res = min(num, res)
                return
            for b in bank:
                diff = 0
                for i in range(len(b)):
                    if b[i] != start[i]: diff += 1
                if diff == 1 and b not in had:
                    num += 1
                    cur = b
                    had.add(b)
                    dfs(cur, end, bank, num)
                    num -= 1
                    had.remove(b)
        dfs(start, end, bank, 0)
        return res if res < 100 else -1

                    
