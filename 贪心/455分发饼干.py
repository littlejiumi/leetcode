class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        num = 0
        g.sort()
        s.sort()
        # 先满足小胃口
        for j in range(len(s)):
            if num < len(g) and s[j] >= g[num]: 
                num += 1
        return num


