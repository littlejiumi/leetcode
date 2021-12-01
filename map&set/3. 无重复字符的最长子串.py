class Solution:  # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxres = 0
        left = 0
        c_dict = {} # dict保存对儿 ch: idx
        for i in range(len(s)):
            if s[i] in c_dict:
                left = max(c_dict[s[i]]+ 1 , left)   # 如果该ch出现过，可能要缩小窗口。注意left放在当前left之后，用max
            maxres = max(maxres, i - left + 1)
            c_dict[s[i]] = i
        return maxres
