class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = [] # 存放分割后的字符
        # 判断数组中的数字是否合法
        if len(s) > 12: return res # 字符串长度最大为12
        def isValid(p):
            if p == '0': return True # 解决"0000"
            if p[0] == '0': return False
            if int(p) > 0 and int(p) <256: return True
            return False

        def backtrack(s, startIndex):
            if len(path) == 4 and startIndex == len(s): # 确保切割完，且切割后的长度为4
                res.append(".".join(path[:])) # 字符拼接
                return

            for i in range(startIndex, len(s)):
                p = s[startIndex:i+1] # 分割字符
                if isValid(p): # 判断字符是否有效
                    path.append(p)
                else: continue
                backtrack(s, i + 1) # 寻找i+1为起始位置的子串
                path.pop()
        backtrack(s, 0)
        return res
