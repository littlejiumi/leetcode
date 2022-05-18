class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        dicS = dict()    # 用来记录最新的s[i]与最新位置i的对应关系
        for i in range(len(s)):  # 右侧是滑动的
            if s[i] in dicS:     # 如果右侧重复了，则更新左边的值，选一个最右的左值
                left = max(left, dicS[s[i]]+1)
            res = max(res, i - left+1)
            dicS[s[i]] = i
        return res
