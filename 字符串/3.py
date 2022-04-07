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
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
