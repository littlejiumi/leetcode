class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:dic[i] = False
            else: dic[i] = True
        for i in s:
            if dic[i]: return i
        return " "
