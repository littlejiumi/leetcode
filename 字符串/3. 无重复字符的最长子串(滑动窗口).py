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
        

 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
        temp = set()
        ans, r = 0, 0
        for i in range(len(s)):
            if i > 0: 
            # 左指针向右移动一格，移除一个字符
                temp.remove(s[i-1])
            while r < len(s) and s[r] not in temp: # 不断地移动右指针
                temp.add(s[r])
                r += 1
            ans = max(ans, r - i)
        return ans
